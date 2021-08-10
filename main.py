try:
    import pandas as pd
except:
    Exception("Instale a biblioteca pandas com o comando pip install pandas")
try:
    from scipy import linalg
    import scipy.sparse as sps
    import scipy.spatial as spa
except:
    Exception("Instale a biblioteca scipy com o comando pip install scipy")
try:
    import matplotlib.pyplot
except:
    Exception("Instale a biblioteca matplotlib com o comando pip install matplotlib")

from lib import util
import sys

arquivo ='dados.txt'
'''
lf = len(sys.argv)
if lf == 1:  # inicia modo demo
    print('Para o modo de demonstração use python main.py demo')
    print('Para verificar o posto adequado use python main.py caminho_arquivo(str)')
    print('')
    print('')
    print('Observação: arquivo deve ter o formato CSV, seprado por ponto e vírgula, duas coluas (origem, genes)')
    exit(0)
elif lf == 2:
    if str(sys.argv[1]) == 'demo':
        arquivo = 'dados.txt'
    else:
        arquivo = sys.argv[1]
'''

try:
    dados = pd.read_csv(arquivo, sep=';')
except:
    Exception("Falha ao ler o arquivo"+arquivo)
    exit(1)

df = pd.DataFrame(dados)
lista = df.to_dict('records')
A = util.montaMatrizNovaDeListaDeDicionarios(lista)
T, S, D = linalg.svd(A)

# Normalizando
soma = 0
Sn = S.copy()
for s in Sn:
    soma += s
for i in range(len(Sn)):
    Sn[i] = Sn[i] * (1 / soma)

# Plotando
matplotlib.pyplot.plot(Sn)
matplotlib.pyplot.plot(Sn, 'o')
frame = matplotlib.pyplot.gca()
frame.get_xaxis().set_visible(False)
matplotlib.pyplot.grid(axis='both')
matplotlib.pyplot.show()