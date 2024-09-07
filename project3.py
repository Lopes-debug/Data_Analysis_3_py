import math
import os, sys
import pandas as pd
import numpy as np
sys.path.append(os.path.abspath(os.path.join('modulos')))
from estrategia1 import *
from estrategia2 import *
from estrategia3 import *

## Telemarketing Data

## Exploratory Analysis
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)
config_na = ['n/a', 'na', 'undefined']

dataset = pd.read_csv(r'C:\Users\leand\OneDrive\Documentos\FormacaoDSA\f_project3\Scripts-P3\dados\dataset.csv', na_values=config_na)
# print(dados.head())

dictionary = pd.read_excel(r'C:\Users\leand\OneDrive\Documentos\FormacaoDSA\f_project3\Scripts-P3\dados\Dicionario.xlsx')
# print(dados_desc.head())

both = pd.concat([pd.Series(dataset.columns.tolist()), dictionary['Fields']],axis=1).rename(columns={0:'Dataset', 'Fields': 'Dicionario'}, inplace=True)
# print(both)
# print(dataset[['Dur. (ms).1', 'Dur. (ms)']])
dataset.rename(columns={'Dur. (ms)': 'Dur. (s)',
                        'Dur. (ms).1':'Dur. (ms)',
                        'Start ms': 'Start Offset (ms)',
                        'End ms': 'End Offset (ms)'}, inplace=True)
# print(dataset.info())
# print(dataset.describe())


## Data Cleaning
# print(help(func_calc_percentual_valores_ausentes))
# func_calc_percentual_valores_ausentes(dataset)

df_missing = func_calc_percentual_valores_ausentes_coluna(dataset)
print(df_missing)
