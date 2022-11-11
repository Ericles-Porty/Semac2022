n = 100000
 
def minimo (x, y):
    if (x < y): 
        return x
    else: 
        return y
 
# Numero de cartas de Alice e de Beatriz
a, b = map(int,input().split())
while(a > 0 and b > 0):
    trocasA = 0
    trocasB = 0
    
    cartasA = [0] * n
    cartasB = [0] * n
    
    cartas = list(map(int, input().split()))
    for i in range(a):
        cartasA[cartas[i]-1] += 1
        
    cartas = list(map(int, input().split()))    
    for i in range(b):
        cartasB[cartas[i]-1] += 1
    
    for i in range(n):
        if (cartasA[i] > 0 and cartasB[i] == 0):
            trocasA += 1
        if (cartasB[i] > 0 and cartasA[i] == 0):
            trocasB += 1
         
    print("{0}".format(minimo(trocasA, trocasB)))
 
    # Relendo o numero de cartas de Alice e de Beatriz
    a, b = map(int,input().split())