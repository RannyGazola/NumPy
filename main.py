# import pandas as pd

# url = "https://raw.githubusercontent.com/alura-cursos/numpy/dados/apples_ts.csv"

# data = pd.read_csv(url)

# data.head()

# print(data)



import numpy as np

url = 'https://raw.githubusercontent.com/alura-cursos/numpy/dados/apples_ts.csv'

dados = np.loadtxt(url,delimiter=',',usecols=np.arange(1,88,1))

print(dados)