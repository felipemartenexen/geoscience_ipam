# -*- coding: utf-8 -*-
"""pogo_analyst.ipynb

Original file is located at
    https://colab.research.google.com/drive/11xieL5OP07_hJSo04k3mLHlhir0zxvDQ
"""

# Importing necessary libraries: Earth Engine (ee) and geemap for geospatial analysis
import ee
import geemap as geemap

# Initializing the Earth Engine API
geemap.ee_initialize()

# Defining various datasets from Earth Engine, including regions of interest, land use, and environmental features
roi = ee.FeatureCollection("users/ipam_flp/Analyses/Restoration_Carbon_Market/Vetor/assentamentos_pogo")
frequency = ee.Image("users/ipam_flp/Analyses/Restoration_Carbon_Market/Image/frequency_pogo_2008_2022")
land_use = ee.Image("projects/mapbiomas-workspace/public/collection8/mapbiomas_collection80_integration_v1").select('classification_2022')
fire_col2 = ee.Image("projects/mapbiomas-workspace/public/collection7_1/mapbiomas-fire-collection2-monthly-burned-coverage-1")
desforestation = ee.FeatureCollection("users/ipam_flp/Analyses/Restoration_Carbon_Market/prodes_2008_2022")
hidro_10 = ee.FeatureCollection("users/ipam_flp/Analyses/Restoration_Carbon_Market/hidro_10m").merge("users/ipam_flp/Analyses/Restoration_Carbon_Market/hidro_10m_lages")
sec_veg = ee.Image("projects/mapbiomas-workspace/public/collection8/mapbiomas_collection80_deforestation_secondary_vegetation_v1").select('classification_2022').eq(303).selfMask()
srtm = ee.Image("USGS/SRTMGL1_003")
region = roi.geometry().buffer(5000)

# Processing the hydrographic data to create a mask for water bodies
hidro_10 = ee.Image().paint(hidro_10, 0, 0.1).remap([0],[1]).clip(region)

# Creating a binary mask for forest land use from the land cover image
forest = ee.Image(1).mask(land_use.eq(3)).clip(roi)
sec_veg = sec_veg.updateMask(forest).clip(roi)

# Setting parameters for identifying significant forest areas based on connected pixel count
minArea = 100000;
maxSize = 500;

pixelCount = forest.connectedPixelCount(maxSize);

minPixelCount = ee.Image(minArea).divide(ee.Image.pixelArea());

forest_gt10ha = forest.updateMask(pixelCount.gte(minPixelCount));

# Filtering the deforestation data to focus on recent years
desforestation = desforestation \
  .filter(ee.Filter.gt('year', (2022 - 5)))

desforestation = ee.Image().paint(desforestation).remap([0],[1]).rename('constant')

# Identifying areas with high fire frequency
fire_more2 = ee.Image(1).mask(frequency.gt(2));

# Creating a composite image to remove areas affected by deforestation and frequent fires
remove_area = ee.ImageCollection([desforestation, fire_more2]).mosaic()

# Calculating the distance from significant forest areas
distanceForest = (
  forest_gt10ha
  .distance(kernel= ee.Kernel.euclidean(200), skipMasked= False)
  .rename('distance')
  .clip(region)
  .selfMask()
)

# Processing elevation data to obtain slope and hillshade information
elevation = srtm.select('elevation').clip(region);
slope = ee.Terrain.slope(elevation).clip(region);
hillshade = ee.Terrain.hillshade(srtm).clip(region);

# Parameters for visualizing distance layer
imageVisParamDistance = {
  "opacity":1,
  "bands":["distance"],
  "min":2,
  "max":8.261297173761164,
  "palette":["bd0026","f03b20","fd8d3c","fecc5c","ffffb2"]
}

imageVisParamDistForest = {
  "opacity": 1,
  "bands": ["distance"],
  "max": 100,
  "palette": ["edf8e9","c7e9c0","a1d99b","74c476","31a354","006d2c"]
}

# Calculating the distance from hydrographic data
distanceHidro = hidro_10 \
  .distance(kernel= ee.Kernel.euclidean(200), skipMasked= False) \
  .rename('distance') \
  .clip(roi) \
  .selfMask()

# Visualization parameters for the hydrographic distance layer
imageVisParamDistHidro = {
  "opacity": 1,
  "bands": ["distance"],
  "max": 100,
  "palette": ["eff3ff","bdd7e7","6baed6", "3182bd","08519c"]
}

# Preparing the region of interest (ROI) for visualization
roi_img = ee.Image().paint(roi)

roi_img = roi_img \
  .remap([0], [1]) \
  .rename('constant')

potencialArea  = roi_img \
  .updateMask(forest_gt10ha.unmask().Not()) \
  .updateMask(remove_area.unmask().Not()) \
  .clip(region)

# Loading a base map layer for visualization
basemap = ee.Image('users/ipam_flp/Analyses/Restoration_Carbon_Market/planet_roi_2023_ago').clip(region)

# Setting visualization parameters for the base map
visBasemap = {'bands':['R','G','B'],'min':150,'max':1000,'gamma':1.3}

# Function to get minimum and maximum values of an image
def get_min_max(image):
  min_max = image.reduceRegion(
      reducer = ee.Reducer.minMax(),
      geometry = region,
      scale = 30,
      maxPixels = 1e9
  )
  return min_max.getInfo()

# Retrieving min and max values
min_max_distanceForest = get_min_max(distanceForest)
min_max_distanceHidro = get_min_max(distanceHidro)
min_max_slope = get_min_max(slope)
min_max_fire_frequency = get_min_max(frequency)

# Normalizing images based on their min and max values
distance_forest_norm = distanceForest.unitScale(min_max_distanceForest['distance_min'], min_max_distanceForest['distance_max'])
distance_hidro_norm = distanceHidro.unitScale(min_max_distanceHidro['distance_min'], min_max_distanceHidro['distance_max'])
slope_norm = slope.unitScale(min_max_slope['slope_min'], min_max_slope['slope_max'])
fire_frequency_norm = frequency.unitScale(min_max_fire_frequency['fire_frequency_min'], min_max_fire_frequency['fire_frequency_max'])

# Defining weights for each variable in the restoration index
weight = {
  'slope': 0.20,
  'fire_frequency': 0.30,
  'distance_hidro': 0.25,
  'distance_forest': 0.25
}

# Calculating the restoration index
index_restoration = distance_forest_norm.multiply(weight['distance_forest']) \
  .add(distance_hidro_norm.multiply(weight['distance_hidro'])) \
  .add(slope_norm.multiply(weight['slope'])) \
  .add(fire_frequency_norm.multiply(weight['fire_frequency'])) \
  .rename('restoration') \
  .mask(potencialArea)

min_max_restoration = get_min_max(index_restoration)
min_max_restoration

# Define the value ranges for each class
class1 = index_restoration.lte(0.1)
class2 = index_restoration.gt(0.1).And(index_restoration.lte(0.2))
class3 = index_restoration.gt(0.2)
class4 = remove_area

# Combine the classes into a single image
index_class = ee.ImageCollection([
    ee.Image(1).mask(class1).toByte(),
    ee.Image(2).mask(class2).toByte(),
    ee.Image(3).mask(class3).toByte(),
    ee.Image(4).mask(class4).toByte()
]).mosaic() \
  .clip(roi)

min_max_classified_index = get_min_max(index_class)
min_max_classified_index

# Setting up the map visualization
map = geemap.Map(height = 800)
map.centerObject(region)

# Adding various layers to the map for visualization
map.addLayer(basemap, visBasemap, '2023-08 planet')
#map.addLayer(potencialArea , {'palete': '#0000ff'}, 'potencialArea', False)
map.addLayer(forest_gt10ha, {'palette': 'green'}, 'Forest', False)
#map.addLayer(sec_veg, {'palette': 'yellow'}, 'sec_veg', False)
#map.addLayer(distanceForest, imageVisParamDistForest, 'Distance - Forest', False)
#map.addLayer(distance_forest_norm, imageVisParamDistForest, 'distance_forest_norm', False)
#map.addLayer(distanceHidro, imageVisParamDistHidro, 'Distance - Hidro', False)
#map.addLayer(elevation, {'min':0, 'max': 300, 'palette': ['90EE90','FFFF00','FF0000']}, 'Raw SRTM', False)
#map.addLayer(hillshade, {'min':150, 'max':255,}, 'Hillshade', False)
#map.addLayer(slope, {'min':0, 'max':20, 'pallete': ['FFFFFF']},'Slope', False)
map.addLayer(remove_area, {},'removeArea', False)
map.addLayer(roi, {},'roi', False)
map.addLayer(index_class, {'min':1, 'max':4, 'palette': ['#a50026', '#fdbf71', '#bde2ee', '#313695']},'classified_index', False)
map.addLayer(hidro_10, {'palette': 'blue'}, 'Hidro_10', False)

# Zonal statistics by group

out_restoration_stats = 'restoration_stats.csv'

geemap.zonal_stats_by_group(
    index_class,
    roi,
    out_restoration_stats,
    stat_type="SUM",
    scale=30,
    denominator=1e4,
    decimal_places=2
)
