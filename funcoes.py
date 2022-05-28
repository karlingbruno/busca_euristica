import csv
import time
def distancia_euclidiana(x1,x2,y1,y2) :
    point1 = [x1,y1]
    point2 = [x2,y2]

    dist =  round(pow(((float(x1) - float(x2)) ** 2) + ((float(y1) - float(y2)) ** 2),0.5))
 
    return(dist)

dados = open('/home/bruno/Documentos/Estudos/Bruno K/instancias/dados.tsp','r')
#Formatando os dados da tabela
vetor = []
index = 0
for linha in dados:
    posicoes = linha.split()
    vetor.insert(index,posicoes[1:3])
    index += 1
    
dados.close()

#calculando as distancias e inserindo na tabela
matriz = []

for linha in range(len(vetor)):
    atual = vetor[linha]
    auxiliar = []
    for coluna in range(len(vetor)):
        auxiliar.append(distancia_euclidiana(atual[0],vetor[coluna][0],atual[1],vetor[coluna][1]))
    
    matriz.insert(linha,auxiliar)

#salvando csv
with open('Saída/Matriz_Adjacencia.csv', "w") as f :
    write = csv.writer(f) 
    write.writerows(matriz)

#Força Bruta
tempo_inicial = time.time()
for linha in range(len(matriz)) : 
    atual = matriz[linha]
    for coluna in range(len(matriz)) : 
        
