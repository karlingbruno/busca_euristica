from math import ceil
import numpy as np

def distancia_euclidiana(x1,x2,y1,y2) :
    a = np.array((x1,y1))
    b = np.array((x2,y2))

    dist = round(np.linalg.norm(a-b))

    print(dist)

#x1 = 5
#x2 = 10
#y1 = 6
#y2 = 15
#distancia_euclidiana(x1,x2,y1,y2)