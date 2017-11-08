import numpy as np

def checagem(matriz):
    aux = matriz[0]
    for x in matriz:
        for (a,b) in zip(aux, x):
            if round(a, 15) != round(b, 15):
                return True
    return False

def markov(matriz):
    while (checagem(matriz)):
        matriz = np.dot(matriz, matriz)
    return matriz

matriz = [[0.25, 0.25, 0.25, 0.25], [0.49, 0.17, 0.22, 0.12], [0.42, 0.02, 0.01, 0.55], [0.97, 0.01, 0.01, 0.01]]

matriz = np.array(matriz)

matriz = markov(matriz)

matriz = np.array(matriz)

for x in matriz:
    print(x)