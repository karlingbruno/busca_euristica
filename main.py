import time
import csv

#Abrindo arquivo
matriz = []
with open ('/home/bruno/Documentos/Estudos/Bruno K/Saída/Matriz_Adjacencia.csv',newline='') as csvfile :
    auxiliar = []
    for linha in csvfile:
        auxiliar = linha.split()
        matriz.append(auxiliar)
        #print(linha)

#for item in matriz:
print(matriz[0][1] + matriz[0][2])




#Aleatório por tempo

#end_time = time.time() + 30
#while time.time() < end_time: 
    

