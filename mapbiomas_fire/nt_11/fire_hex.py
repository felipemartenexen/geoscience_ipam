#%%
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

#%%
# Caminho para o seu shapefile (substitua 'caminho/para/seu/shapefile' pelo caminho correto)
shapefile_path = r'C:\Users\luiz.felipe\Desktop\IPAM\hex_comparativo\shp\hex_amazon.shp'
# Caminhos para os arquivos CSV
fire_hex_2023_path = r'C:\Users\luiz.felipe\Desktop\FLP\MapiaEng\GitHub\geoscience_ipam\mapbiomas_fire\nt_11\data\areas_monitor_fire_hex_amaz_2023.csv'
fire_hex_2022_path = r'C:\Users\luiz.felipe\Desktop\FLP\MapiaEng\GitHub\geoscience_ipam\mapbiomas_fire\nt_11\data\areas_monitor_fire_hex_amaz_2022.csv'

# Carregar e agrupar os dados
df_hex_2023 = pd.read_csv(fire_hex_2023_path)
df_hex_2022 = pd.read_csv(fire_hex_2022_path)


df_hex_2023 = df_hex_2023.groupby('FID')['area'].sum().reset_index()
df_hex_2022 = df_hex_2022.groupby('FID')['area'].sum().reset_index()

# Renomear as colunas de área para indicar o ano
df_hex_2023.rename(columns={'area': 'area_2023'}, inplace=True)
df_hex_2022.rename(columns={'area': 'area_2022'}, inplace=True)

# Combinar os DataFrames com base em 'COD_MUN_NU'
merged_df = pd.merge(df_hex_2023, df_hex_2022, on='FID', how='outer')

# Carregar o shapefile como um GeoDataFrame
gdf = gpd.read_file(shapefile_path)

# Combinar o GeoDataFrame com o DataFrame merged_df baseado em 'COD_MUN_NU'
combined_gdf = gdf.merge(merged_df, on='FID', how='left')

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

#%%Deter
# Caminho para o seu shapefile (substitua 'caminho/para/seu/shapefile' pelo caminho correto)
shapefile_path = r'C:\Users\luiz.felipe\Desktop\IPAM\hex_comparativo\shp\hex_amazon.shp'
# Caminhos para os arquivos CSV
deter_hex_2023_path = r'C:\Users\luiz.felipe\Desktop\FLP\MapiaEng\GitHub\geoscience_ipam\mapbiomas_fire\nt_11\data\areas_deter_hex_amaz_2023.csv'
deter_hex_2022_path = r'C:\Users\luiz.felipe\Desktop\FLP\MapiaEng\GitHub\geoscience_ipam\mapbiomas_fire\nt_11\data\areas_deter_hex_amaz_2022.csv'

# Carregar e agrupar os dados
deter_hex_2023 = pd.read_csv(deter_hex_2023_path)
deter_hex_2022 = pd.read_csv(deter_hex_2022_path)


deter_hex_2023 = deter_hex_2023.groupby('FID')['area'].sum().reset_index()
deter_hex_2022 = deter_hex_2022.groupby('FID')['area'].sum().reset_index()

# Renomear as colunas de área para indicar o ano
deter_hex_2023.rename(columns={'area': 'area_23'}, inplace=True)
deter_hex_2022.rename(columns={'area': 'area_22'}, inplace=True)

# Combinar os DataFrames com base em 'COD_MUN_NU'
merged_df = pd.merge(deter_hex_2023, deter_hex_2022, on='FID', how='outer')

# Carregar o shapefile como um GeoDataFrame
gdf = gpd.read_file(shapefile_path)

# Combinar o GeoDataFrame com o DataFrame merged_df baseado em 'COD_MUN_NU'
combined_deter_gdf = gdf.merge(merged_df, on='FID', how='left')

# Substituir NaN por 0 nas colunas 'area_2023' e 'area_2022'
combined_deter_gdf['area_23'].fillna(0, inplace=True)
combined_deter_gdf['area_22'].fillna(0, inplace=True)
combined_deter_gdf['area_dif'] = combined_deter_gdf['area_23'] - combined_deter_gdf['area_22']

# Exibir o mapa
# Definir o tamanho da figura para plotagem
plt.figure(figsize=(10, 10))

# Primeira plotagem: Preencher as feições com cores baseadas em 'area_dif'
base = combined_deter_gdf.plot(column='area_dif', cmap='PuOr', legend=True,
                         legend_kwds={'label': "Diferença de Área DETER (2023 - 2022)",
                                      'orientation': "horizontal"})

# Segunda plotagem: Adicionar contornos (bordas) às feições
combined_deter_gdf.boundary.plot(ax=base, edgecolor='black', linewidth=0.5)

# Opcional: Configurar título e remover os eixos para uma visualização mais limpa
plt.title('Mapa de Diferença DETER')
plt.axis('off')

# Mostrar o mapa
plt.show()

#%%  Col2 - 85 a 22

# Caminhos definidos para shapefiles e CSV
shapefile_path = r'C:\Users\luiz.felipe\Desktop\IPAM\hex_comparativo\shp\hex_amazon.shp'
base_shapefile_path = r'C:\Users\luiz.felipe\Desktop\IPAM\hex_comparativo\shp\estado_hex_amaz.shp'
col2_hex_path = r'C:\Users\luiz.felipe\Desktop\FLP\MapiaEng\GitHub\geoscience_ipam\mapbiomas_fire\nt_11\data\areas_col2_fire_hex_amaz_85_22.csv'

# Carregar os dados
base_gdf = gpd.read_file(base_shapefile_path)
col2_hex = pd.read_csv(col2_hex_path)

# Processamento dos dados para obter um DataFrame agregado por 'FID' e 'year'
col2_hex_group_year = col2_hex.groupby(['FID', 'year'])['area'].sum().reset_index()
col2_hex_pivot = col2_hex_group_year.pivot_table(index='FID', columns='year', values='area', aggfunc='sum').reset_index()
col2_hex_pivot.fillna(0, inplace=True)

# Carregar o shapefile como um GeoDataFrame e combinar com o DataFrame processado
gdf = gpd.read_file(shapefile_path)
combined_col2_gdf = gdf.merge(col2_hex_pivot, on='FID', how='left')

# Ajuste dos anos considerados e conversão dos nomes das colunas para strings
combined_col2_gdf.columns = combined_col2_gdf.columns.map(str)
anos = [str(ano) for ano in range(1985, 2023)]  # Anos considerados

# Ajustar o layout para remover os dois últimos subplots
n_anos = len(anos) - 2  # Subtraindo dois para excluir os últimos dois anos
n_colunas = 8
n_linhas = (n_anos + n_colunas - 1) // n_colunas  # Calcula o número necessário de linhas
fig, axes = plt.subplots(n_linhas, n_colunas, figsize=(40, 20), sharex=True, sharey=True)

# Achatando o array de axes para facilitar o acesso
axes_flat = axes.flatten()

# Determinar vmin e vmax para normalizar a escala de cores
vmin, vmax = combined_col2_gdf[anos].min().min(), combined_col2_gdf[anos].max().max()

# Iterar sobre os anos (menos os dois últimos) e plotar cada mapa
for i, ano in enumerate(anos):
    ax = axes_flat[i]
    combined_col2_gdf.plot(column=ano, ax=ax, legend=False, cmap='Reds', vmin=vmin, vmax=vmax)
    base_gdf.plot(ax=ax, color='None', edgecolor='grey', linewidth=0.3)
    ax.set_title(f"Ano: {ano}")
    ax.axis('off')

# Removendo os subplots vazios que não serão usados
for j in range(i+1, n_linhas * n_colunas):
    fig.delaxes(axes_flat[j])

# Ajustando a legenda
sm = plt.cm.ScalarMappable(cmap='Reds', norm=plt.Normalize(vmin=vmin, vmax=vmax))
cbar_ax = fig.add_axes([0.92, 0.15, 0.02, 0.7])
fig.colorbar(sm, cax=cbar_ax)

plt.tight_layout(rect=[0, 0, 0.9, 1])
plt.show()

#%%PRODES
# Caminhos definidos para shapefiles e CSV
# Caminho para o seu shapefile (substitua 'caminho/para/seu/shapefile' pelo caminho correto)
shapefile_path = r'C:\Users\luiz.felipe\Desktop\IPAM\hex_comparativo\shp\hex_amazon.shp'
# Caminhos para os arquivos CSV
prodes_hex_2023_path = r'C:\Users\luiz.felipe\Desktop\FLP\MapiaEng\GitHub\geoscience_ipam\mapbiomas_fire\nt_11\data\areas_prodes_pri_2023_hex.csv'

# Carregar e agrupar os dados
df_hex_2023 = pd.read_csv(prodes_hex_2023_path)

df_hex_2023 = df_hex_2023.groupby('FID')['area'].sum().reset_index()

# Renomear as colunas de área para indicar o ano
df_hex_2023.rename(columns={'area': 'area_km2_2023'}, inplace=True)

# Carregar o shapefile como um GeoDataFrame
gdf = gpd.read_file(shapefile_path)

# Combinar o GeoDataFrame com o DataFrame merged_df baseado em 'COD_MUN_NU'
combined_gdf = gdf.merge(df_hex_2023, on='FID', how='left')

# Substituir NaN por 0 nas colunas 'area_2023' e 'area_2022'
combined_gdf['area_km2_2023'].fillna(0, inplace=True)

# Exibir o mapa
# Definir o tamanho da figura para plotagem
plt.figure(figsize=(10, 10))

# Primeira plotagem: Preencher as feições com cores baseadas em 'area_dif'
base = combined_gdf.plot(column='area_km2_2023', cmap='PuOr', legend=True,
                         legend_kwds={'label': "PRODES 2023 (Cenas Prioritárias)",
                                      'orientation': "horizontal"})

# Segunda plotagem: Adicionar contornos (bordas) às feições
combined_gdf.boundary.plot(ax=base, edgecolor='black', linewidth=0.5)

# Opcional: Configurar título e remover os eixos para uma visualização mais limpa
plt.title('PRODES 2023 (Cenas Prioritárias)')
plt.axis('off')

# Mostrar o mapa
plt.show()

#%% Join tables

#%%Exportar
# Definir o caminho de destino para o shapefile exportado
output_path = r'C:\Users\luiz.felipe\Desktop\FLP\MapiaEng\GitHub\geoscience_ipam\mapbiomas_fire\nt_11\shp\areas_prodes_hex_2023.shp'

combined_gdf.fillna(0, inplace=True)

# Exportar o combined_gdf como um shapefile
combined_gdf.to_file(output_path)

print("Exportado")
# %%

