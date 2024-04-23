#%%
import pandas as pd

#%%
data_2022 = pd.read_csv(r'C:\Users\luiz.felipe\Desktop\FLP\MapiaEng\GitHub\geoscience_ipam\mapbiomas_fire\nt_11\data\areas-fundiario-landuse-fire-2022-amazonia.csv')
data_2023 = pd.read_csv(r'C:\Users\luiz.felipe\Desktop\FLP\MapiaEng\GitHub\geoscience_ipam\mapbiomas_fire\nt_11\data\areas-fundiario-landuse-fire-2023-amazonia.csv')

data = pd.concat([data_2022, data_2023], ignore_index=True)

data = data.drop(columns=['system:index', '.geo'])

# Criar novas colunas 'land_use' e 'fundiario' com as operações especificadas
data['land_use'] = data['class'] // 1000
data['fundiario'] = data['class'] % 1000

class_lulc = {
    1:  'Floresta', #'Floresta',
    3:  'Floresta', #'Formação Florestal', 
    4:  'Savana', #'Formação Savânica', 
    5:  'Floresta', #'Mangue', 
    6:  'Floresta', #'Floresta Alagável (beta)', 
    49: 'Floresta', #'Restinga Florestal', 
    10: 'Outros', #'Formação Natural não Florestal',
    11: 'Outros', #'Área Úmida Natural não Florestal', 
    12: 'Campo', #'Formação Campestre', 
    32: 'Outros', #'Apicum', 
    29: 'Outros', #'Afloramento Rochoso', 
    50: 'Outros', #'Restinga Herbácea', 
    13: 'Outros', #'Outra Formação não Florestal', 
    18: 'Agricultura', #'Agricultura', 
    39: 'Agricultura', #'Soja', 
    20: 'Agricultura', #'Cana', 
    40: 'Agricultura', #'Arroz', 
    62: 'Agricultura', #'Algodão', 
    41: 'Agricultura', #'Outras Lavouras Temporárias', 
    46: 'Agricultura', #'Café', 
    47: 'Agricultura', #'Citrus', 
    35: 'Agricultura', #'Dendê', 
    48: 'Agricultura', #'Outras Lavaouras Perenes', 
    9:  'Agricultura', #'Silvicultura', 
    15: 'Pecuaria', #'Pastagem', 
    21: 'Mosaico', #'Mosaico de Agricultura ou Pastagem', 
    22: 'Outros', #'Área não Vegetada', 
    23: 'Outros', #'Praia e Duna', 
    24: 'Outros', #'Área Urbanizada', 
    30: 'Outros', #'Mineração', 
    25: 'Outros', #'Outra Área não Vegetada', 
    33: 'Outros', #'Rio, Lago e Oceano', 
    31: 'Outros', #'Aquicultura'
}

class_fundiario = {
1:	'Sem Informação',#'SI',
2:	'Terra Indígena',#'TIh',
3:	'Terra Indígena',#'TInh',
4:	'UCs Proteção Integral',#'UCPI FED',
5:	'UCs Proteção Integral',#'UCPI EST',
6:	'UCs Proteção Integral',#'UCPI MUN',
7:	'UCs Sustentável',#'UCUS FED',
8:	'UCs Sustentável',#'UCUS EST',
9:	'UCs Sustentável',#'UCUS MUN',
10:	'Area militar',#'Area militar',
11:	'Quilombos',#'Territorio quilombola Federal',
12:	'Quilombos',#'Territorio quilombola estadual',
13:	'Assentamento',#'PA diferenciados federais',
14:	'Assentamento',#'PA outros federais',
15:	'Assentamento',#'PA outros estaduais',
16:	'Assentamento',#'PA outros municipais',
17:	'UCs Sustentável',#'APA_ARIE FEDERAL',
18:	'UCs Sustentável',#'APA_ARIE ESTADUAL',
19:	'UCs Sustentável',#'APA_ARIE MUNICIPAL',
20:	'Imóveis Privados SIGEF',#'SIGEF priv peq',
21:	'Imóveis Privados SIGEF',#'SIGEF priv  med',
22:	'Imóveis Privados SIGEF',#'SIGEF priv grd',
23:	'Florestas Públicas Não Destinadas',#'FPND FEDERAIS',
24:	'Florestas Públicas Não Destinadas',#'FPND ESTADUAIS',
25:	'Terras Públicas',#'Glb federais',
26:	'Terras Públicas',#'Glb estaduais',
100:'Imóveis Privados CAR',# 'CAR Pequeno ativo ou pendente sem sobreposição',
102:'Imóveis Privados CAR',# 'CAR PEQ ativo ou pendente  sobreposição com TIh',
103:'Imóveis Privados CAR',# 'CAR PEQ ativo ou pendente  sobreposição com TInh',
104:'Imóveis Privados CAR',# 'CAR PEQ ativo ou pendente  sobreposição com UCPI FED',
105:'Imóveis Privados CAR',# 'CAR PEQ ativo ou pendente  sobreposição com UCPI EST',
106:'Imóveis Privados CAR',# 'CAR PEQ ativo ou pendente  sobreposição com UCPI MUN',
107:'Imóveis Privados CAR',# 'CAR PEQ ativo ou pendente  sobreposição com UCUS FED',
108:'Imóveis Privados CAR',# 'CAR PEQ ativo ou pendente  sobreposição com UCUS EST',
109:'Imóveis Privados CAR',# 'CAR PEQ ativo ou pendente  sobreposição com UCUS MUN',
110:'Imóveis Privados CAR',# 'CAR PEQ ativo ou pendente  sobreposição com Area militar',
111:'Imóveis Privados CAR',# 'CAR PEQ ativo ou pendente  sobreposição com Territorio quilombola Federal',
112:'Imóveis Privados CAR',# 'CAR PEQ ativo ou pendente  sobreposição com Territorio quilombola estadual',
113:'Imóveis Privados CAR',# 'CAR PEQ ativo ou pendente  sobreposição com PA diferenciados federais',
114:'Imóveis Privados CAR',# 'CAR PEQ ativo ou pendente  sobreposição com PA outros federais',
115:'Imóveis Privados CAR',# 'CAR PEQ ativo ou pendente  sobreposição com PA outros estaduais',
116:'Imóveis Privados CAR',# 'CAR PEQ ativo ou pendente  sobreposição com PA outros municipais',
117:'Imóveis Privados CAR',# 'CAR PEQ ativo ou pendente  sobreposição com APA_ARIE FEDERAL',
118:'Imóveis Privados CAR',# 'CAR PEQ ativo ou pendente  sobreposição com APA_ARIE ESTADUAL',
119:'Imóveis Privados CAR',# 'CAR PEQ ativo ou pendente  sobreposição com APA_ARIE MUNICIPAL',
120:'Imóveis Privados CAR',# 'CAR PEQ ativo ou pendente  sobreposição com SIGEF priv peq',
121:'Imóveis Privados CAR',# 'CAR PEQ ativo ou pendente  sobreposição com SIGEF priv  med',
122:'Imóveis Privados CAR',# 'CAR PEQ ativo ou pendente  sobreposição com SIGEF priv grd',
123:'Floresta Pública Não Destinada/CAR',# 'CAR PEQ ativo ou pendente  sobreposição com FPND FEDERAIS',
124:'Floresta Pública Não Destinada/CAR',# 'CAR PEQ ativo ou pendente  sobreposição com FPND ESTADUAIS',
125:'Imóveis Privados CAR',# 'CAR PEQ ativo ou pendente  sobreposição com Glb federais',
126:'Imóveis Privados CAR',# 'CAR PEQ ativo ou pendente  sobreposição com Glb estaduais',
200:'Imóveis Privados CAR',# 'CAR medio ativo ou pendente sem sobreposição',
202:'Imóveis Privados CAR',# 'CAR MED ativo ou pendente  sobreposição com TIh',
203:'Imóveis Privados CAR',# 'CAR MED ativo ou pendente  sobreposição com TInh',
204:'Imóveis Privados CAR',# 'CAR MED ativo ou pendente  sobreposição com UCPI FED',
205:'Imóveis Privados CAR',# 'CAR MED ativo ou pendente  sobreposição com UCPI EST',
206:'Imóveis Privados CAR',# 'CAR MED ativo ou pendente  sobreposição com UCPI MUN',
207:'Imóveis Privados CAR',# 'CAR MED ativo ou pendente  sobreposição com UCUS FED',
208:'Imóveis Privados CAR',# 'CAR MED ativo ou pendente  sobreposição com UCUS EST',
209:'Imóveis Privados CAR',# 'CAR MED ativo ou pendente  sobreposição com UCUS MUN',
210:'Imóveis Privados CAR',# 'CAR MED ativo ou pendente  sobreposição com Area militar',
211:'Imóveis Privados CAR',# 'CAR MED ativo ou pendente  sobreposição com Territorio quilombola Federal',
212:'Imóveis Privados CAR',# 'CAR MED ativo ou pendente  sobreposição com Territorio quilombola estadual',
213:'Imóveis Privados CAR',# 'CAR MED ativo ou pendente  sobreposição com PA diferenciados federais',
214:'Imóveis Privados CAR',# 'CAR MED ativo ou pendente  sobreposição com PA outros federais',
215:'Imóveis Privados CAR',# 'CAR MED ativo ou pendente  sobreposição com PA outros estaduais',
216:'Imóveis Privados CAR',# 'CAR MED ativo ou pendente  sobreposição com PA outros municipais',
217:'Imóveis Privados CAR',# 'CAR MED ativo ou pendente  sobreposição com APA_ARIE FEDERAL',
218:'Imóveis Privados CAR',# 'CAR MED ativo ou pendente  sobreposição com APA_ARIE ESTADUAL',
219:'Imóveis Privados CAR',# 'CAR MED ativo ou pendente  sobreposição com APA_ARIE MUNICIPAL',
220:'Imóveis Privados CAR',# 'CAR MED ativo ou pendente  sobreposição com SIGEF priv peq',
221:'Imóveis Privados CAR',# 'CAR MED ativo ou pendente  sobreposição com SIGEF priv  med',
222:'Imóveis Privados CAR',# 'CAR MED ativo ou pendente  sobreposição com SIGEF priv grd',
223:'Floresta Pública Não Destinada/CAR',# 'CAR MED ativo ou pendente  sobreposição com FPND FEDERAIS',
224:'Floresta Pública Não Destinada/CAR',# 'CAR MED ativo ou pendente  sobreposição com FPND ESTADUAIS',
225:'Imóveis Privados CAR',# 'CAR MED ativo ou pendente  sobreposição com Glb federais',
226:'Imóveis Privados CAR',# 'CAR MED ativo ou pendente  sobreposição com Glb estaduais',
300:'Imóveis Privados CAR',# 'CAR grande Ativo ou pendente sem sobreposição',
302:'Imóveis Privados CAR',# 'CAR GRDE ativo ou pendente  sobreposição com TIh',
303:'Imóveis Privados CAR',# 'CAR GRDE ativo ou pendente  sobreposição com TInh',
304:'Imóveis Privados CAR',# 'CAR GRDE ativo ou pendente  sobreposição com UCPI FED',
305:'Imóveis Privados CAR',# 'CAR GRDE ativo ou pendente  sobreposição com UCPI EST',
306:'Imóveis Privados CAR',# 'CAR GRDE ativo ou pendente  sobreposição com UCPI MUN',
307:'Imóveis Privados CAR',# 'CAR GRDE ativo ou pendente  sobreposição com UCUS FED',
308:'Imóveis Privados CAR',# 'CAR GRDE ativo ou pendente  sobreposição com UCUS EST',
309:'Imóveis Privados CAR',# 'CAR GRDE ativo ou pendente  sobreposição com UCUS MUN',
310:'Imóveis Privados CAR',# 'CAR GRDE ativo ou pendente  sobreposição com Area militar',
311:'Imóveis Privados CAR',# 'CAR GRDE ativo ou pendente  sobreposição com Territorio quilombola Federal',
312:'Imóveis Privados CAR',# 'CAR GRDE ativo ou pendente  sobreposição com Territorio quilombola estadual',
313:'Imóveis Privados CAR',# 'CAR GRDE ativo ou pendente  sobreposição com PA diferenciados federais',
314:'Imóveis Privados CAR',# 'CAR GRDE ativo ou pendente  sobreposição com PA outros federais',
315:'Imóveis Privados CAR',# 'CAR GRDE ativo ou pendente  sobreposição com PA outros estaduais',
316:'Imóveis Privados CAR',# 'CAR GRDE ativo ou pendente  sobreposição com PA outros municipais',
317:'Imóveis Privados CAR',# 'CAR GRDE ativo ou pendente  sobreposição com APA_ARIE FEDERAL',
318:'Imóveis Privados CAR',# 'CAR GRDE ativo ou pendente  sobreposição com APA_ARIE ESTADUAL',
319:'Imóveis Privados CAR',# 'CAR GRDE ativo ou pendente  sobreposição com APA_ARIE MUNICIPAL',
320:'Imóveis Privados CAR',# 'CAR GRDE ativo ou pendente  sobreposição com SIGEF priv peq',
321:'Imóveis Privados CAR',# 'CAR GRDE ativo ou pendente  sobreposição com SIGEF priv  med',
322:'Imóveis Privados CAR',# 'CAR GRDE ativo ou pendente  sobreposição com SIGEF priv grd',
323:'Floresta Pública Não Destinada/CAR',# 'CAR GRDE ativo ou pendente  sobreposição com FPND FEDERAIS',
324:'Floresta Pública Não Destinada/CAR',# 'CAR GRDE ativo ou pendente  sobreposição com FPND ESTADUAIS',
325:'Imóveis Privados CAR',# 'CAR GRDE ativo ou pendente  sobreposição com Glb federais',
326:'Imóveis Privados CAR',# 'CAR GRDE ativo ou pendente  sobreposição com Glb estaduais',
400:'Imóveis Privados CAR',# 'CAR pequeno cancelado ou suspenso sem sobreposição',
402:'Imóveis Privados CAR',# 'CAR PEQ cancelado ou suspenso sobreposição com TIh',
403:'Imóveis Privados CAR',# 'CAR PEQ cancelado ou suspenso sobreposição com TInh',
404:'Imóveis Privados CAR',# 'CAR PEQ cancelado ou suspenso sobreposição com UCPI FED',
405:'Imóveis Privados CAR',# 'CAR PEQ cancelado ou suspenso sobreposição com UCPI EST',
406:'Imóveis Privados CAR',# 'CAR PEQ cancelado ou suspenso sobreposição com UCPI MUN',
407:'Imóveis Privados CAR',# 'CAR PEQ cancelado ou suspenso sobreposição com UCUS FED',
408:'Imóveis Privados CAR',# 'CAR PEQ cancelado ou suspenso sobreposição com UCUS EST',
410:'Imóveis Privados CAR',# 'CAR PEQ cancelado ou suspenso sobreposição com Area militar',
411:'Imóveis Privados CAR',# 'CAR PEQ cancelado ou suspenso sobreposição com Territorio quilombola Federal',
412:'Imóveis Privados CAR',# 'CAR PEQ cancelado ou suspenso sobreposição com Territorio quilombola estadual',
413:'Imóveis Privados CAR',# 'CAR PEQ cancelado ou suspenso sobreposição com PA diferenciados federais',
414:'Imóveis Privados CAR',# 'CAR PEQ cancelado ou suspenso sobreposição com PA outros federais',
415:'Imóveis Privados CAR',# 'CAR PEQ cancelado ou suspenso sobreposição com PA outros estaduais',
416:'Imóveis Privados CAR',# 'CAR PEQ cancelado ou suspenso sobreposição com PA outros municipais',
417:'Imóveis Privados CAR',# 'CAR PEQ cancelado ou suspenso sobreposição com APA_ARIE FEDERAL',
418:'Imóveis Privados CAR',# 'CAR PEQ cancelado ou suspenso sobreposição com APA_ARIE ESTADUAL',
419:'Imóveis Privados CAR',# 'CAR PEQ cancelado ou suspenso sobreposição com APA_ARIE MUNICIPAL',
420:'Imóveis Privados CAR',# 'CAR PEQ cancelado ou suspenso sobreposição com SIGEF priv peq',
421:'Imóveis Privados CAR',# 'CAR PEQ cancelado ou suspenso sobreposição com SIGEF priv  med',
422:'Imóveis Privados CAR',# 'CAR PEQ cancelado ou suspenso sobreposição com SIGEF priv grd',
423:'Floresta Pública Não Destinada/CAR',# 'CAR PEQ cancelado ou suspenso sobreposição com FPND FEDERAIS',
424:'Floresta Pública Não Destinada/CAR',# 'CAR PEQ cancelado ou suspenso sobreposição com FPND ESTADUAIS',
425:'Imóveis Privados CAR',# 'CAR PEQ cancelado ou suspenso sobreposição com Glb federais',
426:'Imóveis Privados CAR',# 'CAR PEQ cancelado ou suspenso sobreposição com Glb estaduais',
500:'Imóveis Privados CAR',# 'CAR medio cancelado ou suspenso sem sobreposição',
502:'Imóveis Privados CAR',# 'CAR MED cancelado ou suspenso sobreposição com TIh',
503:'Imóveis Privados CAR',# 'CAR MED cancelado ou suspenso sobreposição com TInh',
504:'Imóveis Privados CAR',# 'CAR MED cancelado ou suspenso sobreposição com UCPI FED',
505:'Imóveis Privados CAR',# 'CAR MED cancelado ou suspenso sobreposição com UCPI EST',
506:'Imóveis Privados CAR',# 'CAR MED cancelado ou suspenso sobreposição com UCPI MUN',
507:'Imóveis Privados CAR',# 'CAR MED cancelado ou suspenso sobreposição com UCUS FED',
508:'Imóveis Privados CAR',# 'CAR MED cancelado ou suspenso sobreposição com UCUS EST',
509:'Imóveis Privados CAR',# 'CAR MED cancelado ou suspenso sobreposição com UCUS MUN',
510:'Imóveis Privados CAR',# 'CAR MED cancelado ou suspenso sobreposição com Area militar',
511:'Imóveis Privados CAR',# 'CAR MED cancelado ou suspenso sobreposição com Territorio quilombola Federal',
512:'Imóveis Privados CAR',# 'CAR MED cancelado ou suspenso sobreposição com Territorio quilombola estadual',
513:'Imóveis Privados CAR',# 'CAR MED cancelado ou suspenso sobreposição com PA diferenciados federais',
514:'Imóveis Privados CAR',# 'CAR MED cancelado ou suspenso sobreposição com PA outros federais',
515:'Imóveis Privados CAR',# 'CAR MED cancelado ou suspenso sobreposição com PA outros estaduais',
516:'Imóveis Privados CAR',# 'CAR MED cancelado ou suspenso sobreposição com PA outros municipais',
517:'Imóveis Privados CAR',# 'CAR MED cancelado ou suspenso sobreposição com APA_ARIE FEDERAL',
518:'Imóveis Privados CAR',# 'CAR MED cancelado ou suspenso sobreposição com APA_ARIE ESTADUAL',
519:'Imóveis Privados CAR',# 'CAR MED cancelado ou suspenso sobreposição com APA_ARIE MUNICIPAL',
520:'Imóveis Privados CAR',# 'CAR MED cancelado ou suspenso sobreposição com SIGEF priv peq',
521:'Imóveis Privados CAR',# 'CAR MED cancelado ou suspenso sobreposição com SIGEF priv  med',
522:'Imóveis Privados CAR',# 'CAR MED cancelado ou suspenso sobreposição com SIGEF priv grd',
523:'Floresta Pública Não Destinada/CAR',# 'CAR MED cancelado ou suspenso sobreposição com FPND FEDERAIS',
524:'Floresta Pública Não Destinada/CAR',# 'CAR MED cancelado ou suspenso sobreposição com FPND ESTADUAIS',
525:'Imóveis Privados CAR',# 'CAR MED cancelado ou suspenso sobreposição com Glb federais',
526:'Imóveis Privados CAR',# 'CAR MED cancelado ou suspenso sobreposição com Glb estaduais',
600:'Imóveis Privados CAR',# 'CAR grande cancelado ou suspenso sem sobreposição',
602:'Imóveis Privados CAR',# 'CAR GRDE cancelado ou suspenso sobreposição com TIh',
603:'Imóveis Privados CAR',# 'CAR GRDE cancelado ou suspenso sobreposição com TInh',
604:'Imóveis Privados CAR',# 'CAR GRDE cancelado ou suspenso sobreposição com UCPI FED',
605:'Imóveis Privados CAR',# 'CAR GRDE cancelado ou suspenso sobreposição com UCPI EST',
606:'Imóveis Privados CAR',# 'CAR GRDE cancelado ou suspenso sobreposição com UCPI MUN',
607:'Imóveis Privados CAR',# 'CAR GRDE cancelado ou suspenso sobreposição com UCUS FED',
608:'Imóveis Privados CAR',# 'CAR GRDE cancelado ou suspenso sobreposição com UCUS EST',
609:'Imóveis Privados CAR',# 'CAR GRDE cancelado ou suspenso sobreposição com UCUS MUN',
610:'Imóveis Privados CAR',# 'CAR GRDE cancelado ou suspenso sobreposição com Area militar',
611:'Imóveis Privados CAR',# 'CAR GRDE cancelado ou suspenso sobreposição com Territorio quilombola Federal',
612:'Imóveis Privados CAR',# 'CAR GRDE cancelado ou suspenso sobreposição com Territorio quilombola estadual',
613:'Imóveis Privados CAR',# 'CAR GRDE cancelado ou suspenso sobreposição com PA diferenciados federais',
614:'Imóveis Privados CAR',# 'CAR GRDE cancelado ou suspenso sobreposição com PA outros federais',
615:'Imóveis Privados CAR',# 'CAR GRDE cancelado ou suspenso sobreposição com PA outros estaduais',
616:'Imóveis Privados CAR',# 'CAR GRDE cancelado ou suspenso sobreposição com PA outros municipais',
617:'Imóveis Privados CAR',# 'CAR GRDE cancelado ou suspenso sobreposição com APA_ARIE FEDERAL',
618:'Imóveis Privados CAR',# 'CAR GRDE cancelado ou suspenso sobreposição com APA_ARIE ESTADUAL',
619:'Imóveis Privados CAR',# 'CAR GRDE cancelado ou suspenso sobreposição com APA_ARIE MUNICIPAL',
620:'Imóveis Privados CAR',# 'CAR GRDE cancelado ou suspenso sobreposição com SIGEF priv peq',
621:'Imóveis Privados CAR',# 'CAR GRDE cancelado ou suspenso sobreposição com SIGEF priv  med',
622:'Imóveis Privados CAR',# 'CAR GRDE cancelado ou suspenso sobreposição com SIGEF priv grd',
623:'Floresta Pública Não Destinada/CAR',# 'CAR GRDE cancelado ou suspenso sobreposição com FPND FEDERAIS',
624:'Floresta Pública Não Destinada/CAR',# 'CAR GRDE cancelado ou suspenso sobreposição com FPND ESTADUAIS',
625:'Imóveis Privados CAR',# 'CAR GRDE cancelado ou suspenso sobreposição com Glb federais',
626:'Imóveis Privados CAR',# 'CAR GRDE cancelado ou suspenso sobreposição com Glb estaduais',
700:'Outros',# 'agua'
}

data['desc_fund'] = data['fundiario'].map(class_fundiario)

data['desc_land_use'] = data['land_use'].map(class_lulc)

data_grouped = data.groupby(['year', 'desc_fund', 'desc_land_use'])['area'].sum().reset_index()

data_grouped = data_grouped[((data_grouped['year'] == 2022))]

data_grouped['fundiaria_amazonia'] = data_grouped['desc_fund']

pivot_table = data_grouped.pivot_table(
    values='area', 
    index='fundiaria_amazonia', 
    columns='desc_land_use', 
    aggfunc='sum', 
    fill_value=0
)

# Ordenar as colunas de 'land_use' conforme solicitado
try:
    # Reorganizar as colunas para garantir a ordem 1, 2, 3, 4
    desired_order = ['Floresta', 'Savana', 'Campo', 'Agricultura', 'Pecuaria', 'Mosaico', 'Outros'
]
    existing_columns = [col for col in desired_order if col in pivot_table.columns]
    ordered_pivot_table = pivot_table[existing_columns]
    ordered_pivot_table.head()
except Exception as e:
    ordered_pivot_table = str(e)  # Se houver erro, captura a mensagem de erro

ordered_pivot_table

print(ordered_pivot_table)

#print(data_grouped[(data_grouped['desc_fund'] == 'Assentamento') & ((data_grouped['year'] == 2022))])

# %%

# Definir o caminho de destino para o shapefile exportado
output_path = r'C:\Users\luiz.felipe\Desktop\FLP\MapiaEng\GitHub\geoscience_ipam\mapbiomas_fire\nt_11\data\areas_fund_fire_lulc_2022.csv'

ordered_pivot_table.fillna(0, inplace=True)

# Exportar o combined_gdf como um shapefile
ordered_pivot_table.to_csv(output_path)

print("Exportado")
