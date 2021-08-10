try:
    import numpy as np
except:
    Exception("Instale a biblioteca numpy com o comando pip install numpy")
import re
import csv

def criapos(janela6: str) -> int:
    if not re.search('(G|C|A|T)*', janela6) or len(janela6) != 6:
        raise Exception('ERRO AO TRATAR A JANELA ', janela6)
    if janela6.count('N')>0:
        #print('Janela inválida: ', janela6)
        return 0
    alfabeto = 'GCAT'
    p1 = alfabeto.find(janela6[0]) + 1  # se não encontra, o valor será zero ao invés de -1
    p2 = alfabeto.find(janela6[1]) + 1
    p3 = alfabeto.find(janela6[2]) + 1
    p4 = alfabeto.find(janela6[3]) + 1
    p5 = alfabeto.find(janela6[4]) + 1
    p6 = alfabeto.find(janela6[5]) + 1
    return 1024 * (p1 - 1) + 256 * (p2 - 1) + 64 * (p3 - 1) + 16 * (p4 - 1) + 4 * (p5 - 1) + p6 -1 # -1 no Matlab a primeira posição do vetor é 1, aqui é 0


def slidwindow6(sequencia: str) -> list:
    frequencia = np.zeros(4096, dtype=int)
    sequencia = sequencia.strip()
    sequencia = sequencia.upper()
    tamanho = len(sequencia)
    for i in range(tamanho-5):
        janela = sequencia[i] + sequencia[i + 1] + sequencia[i + 2] + sequencia[i + 3] + sequencia[i + 4] + sequencia[
            i + 5]
        p = criapos(janela)
        if p!=0:
            frequencia[p] = frequencia[p] + 1
    return frequencia


def montaMatrizNovaDeListaDeDicionarios(lista: list) -> list:
    A = np.zeros((4096, len(lista)), dtype=int)
    itemLista = -1
    for dic in lista:
        itemLista = itemLista + 1
        s = dic.get('genes')
        f = slidwindow6(s)
        for linha in range(4096):
            A[linha][itemLista] = f[linha]
    #Salva matriz em arquivo
    with open('myfile.csv', 'w', newline='') as file:
        mywriter = csv.writer(file, delimiter=',')
        mywriter.writerows(A)
    return A

def normaliza1(Sn: list) -> list:
    soma=0

    for s in Sn:
        soma += s
    for i in range(len(Sn)):
        Sn[i] = Sn[i] * (1/soma)
    return Sn