import numpy as np
def distancia_euclidiana(x1,x2,y1,y2) :
    a = np.array((x1,y1))
    b = np.array((x2,y2))

    dist = round(np.linalg.norm(a-b))

    return(dist)

dados = open('/home/aluno/Documentos/Bruno K/Instancia/dados.tsp','r')

vetor = []
index = 0
for linha in dados:
    posicoes = linha.split()
    vetor.insert(index,posicoes[1:3])
    index += 1
#print(vetor)
dados.close()

matriz = np.array([])

#for linha in vetor:
 #   for coluna in vetor : 
  #      numpy.insert(matriz,linha, coluna)
linha = 0 
coluna = 0
while linha <= np.size(vetor) :
    xBase = vetor[linha][0]
    yBase = vetor[linha][1]
    while coluna <= np.size(vetor):
        distancia = distancia_euclidiana(xBase,vetor[coluna][0],yBase,vetor[coluna][1])
        print(distancia)
        coluna += 1
    linha += 1
    