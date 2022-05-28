from math import ceil
import numpy as np

def distancia_euclidiana(x1,x2,y1,y2) :
    point1 = [x1,y1]
    point2 = [x2,y2]

    dist =  pow(((x1 - x2) ** 2) + ((y1 - y2) ** 2),0.5)
 
    return(dist)
x1 = 20833.3333
x2 = 20833.3333
y1 = 17100.0000
y2 = 17100.0000
print(round(distancia_euclidiana(x1,x2,y1,y2)))