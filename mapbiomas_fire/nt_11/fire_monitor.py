#%%
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Caminho para o seu shapefile (substitua 'caminho/para/seu/shapefile' pelo caminho correto)
shapefile_path = r'C:\Users\luiz.felipe\Desktop\IPAM\shp\municipios_amazonia_2.shp'
# Caminhos para os arquivos CSV
fire_2023_path = r'C:\Users\luiz.felipe\Downloads\map_drive-download-20240220T202909Z-001\areas_fire_mun_amaz_2023.csv'
fire_2022_path = r'C:\Users\luiz.felipe\Downloads\map_drive-download-20240220T202909Z-001\areas_fire_mun_amaz_2022.csv'

# Carregar e agrupar os dados
df_2023 = pd.read_csv(fire_2023_path).groupby('COD_MUN_NU')['area'].sum().reset_index()
df_2022 = pd.read_csv(fire_2022_path).groupby('COD_MUN_NU')['area'].sum().reset_index()

# Renomear as colunas de área para indicar o ano
df_2023.rename(columns={'area': 'area_2023'}, inplace=True)
df_2022.rename(columns={'area': 'area_2022'}, inplace=True)

# Combinar os DataFrames com base em 'COD_MUN_NU'
merged_df = pd.merge(df_2023, df_2022, on='COD_MUN_NU', how='outer')

# Carregar o shapefile como um GeoDataFrame
gdf = gpd.read_file(shapefile_path)

# Combinar o GeoDataFrame com o DataFrame merged_df baseado em 'COD_MUN_NU'
combined_gdf = gdf.merge(merged_df, on='COD_MUN_NU', how='left')

# Substituir NaN por 0 nas colunas 'area_2023' e 'area_2022'
combined_gdf['area_2023'].fillna(0, inplace=True)
combined_gdf['area_2022'].fillna(0, inplace=True)
combined_gdf['area_dif'] = combined_gdf['area_2023'] - combined_gdf['area_2022']

# Exibir o mapa
# Definir o tamanho da figura para plotagem
plt.figure(figsize=(10, 10))

# Primeira plotagem: Preencher as feições com cores baseadas em 'area_dif'
base = combined_gdf.plot(column='area_dif', cmap='PuOr', legend=True,
                         legend_kwds={'label': "Diferença de Área de Incêndio (2023 - 2022)",
                                      'orientation': "horizontal"})

# Segunda plotagem: Adicionar contornos (bordas) às feições
combined_gdf.boundary.plot(ax=base, edgecolor='black', linewidth=0.5)

# Opcional: Configurar título e remover os eixos para uma visualização mais limpa
plt.title('Mapa de Diferença de Área de Incêndio com Contornos')
plt.axis('off')

# Mostrar o mapa
plt.show()

# %%
# Definir o caminho de destino para o shapefile exportado
output_path = r'C:\Users\luiz.felipe\Downloads\map_drive-download-20240220T202909Z-001\combined_gdf.shp'

# Exportar o combined_gdf como um shapefile
combined_gdf.to_file(output_path)
