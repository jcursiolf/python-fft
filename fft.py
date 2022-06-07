import pandas as pd
import numpy as np
from numpy.fft import fft, ifft

# Inicialmente importamos o `pandas`, com delimitador como vírgula. Os dados precisam usar ponto para decimal, exemplo: 0.31416.
# O argumento `usecols =['Tempo','Axial','Horizontal','Vertical']` diz quais colunas queremos. Se precisar ignorar uma, é só tirar.
# A coluna "pontos" não é necessária pq o pandas já cria uma coluna index automaticamente.
# Se usar alguma coluna com `[]` no nome, é preciso renomear `[g]` para `g` para o Python não confundir com um vetor.
# O `print(df.dtypes)` é pra retornar o tipo dos dados lidos. Esperamos `float` (decimal).

print("Abrindo arquivo FormaOnda2.csv.")
df = pd.read_csv('FormaOnda2.csv', delimiter=',', usecols =['Tempo','Axial','Horizontal','Vertical'])
# df.rename(columns={'[g]':'g'}, inplace=True)
print(df.dtypes)
print("Se todos os tipos acima forem float64 (ou alguma variação de float), está tudo OK.")

# Cálculos
X1 = fft(df['Axial']) # FFT
X2 = fft(df['Horizontal']) # FFT
X3 = fft(df['Vertical']) # FFT
N = len(df['Tempo']) # número de pontos
n = np.arange(N) #cria um vetor de tamanho N para ser usado como a coluna "pontos" do CSV
interval = df['Tempo'][N-1] - df['Tempo'][0] # intervalo da amostra
sr = N/interval # sampling rate
T = N/sr # Período
freq = n/T
t=df['Tempo']

# Exportando para CSV
data = { 'Frequencia': freq, 'Axial': np.abs(X1), 'Horizontal': np.abs(X2), 'Vertical' : np.abs(X3)}
result_df = pd.DataFrame(data)
result_df.to_csv('result_python.csv')
print("Resultados salvos como result_python.csv")
