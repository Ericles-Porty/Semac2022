melhor_i = 0
melhor_f = 0
t = 1

while True:
    n = int(input())
    
    if n == 0:
        break
    
    soma = 0
    melhor = -1
    iTemp = 1
    i = 0
    
    while n > 0:
        i += 1
        x, y = map(int, input().split())
        soma += (x - y)
        if soma < 0:
            soma = 0
            iTemp = i + 1
        elif soma > 0 and (soma > melhor or (soma == melhor and i-iTemp >= melhor_f - melhor_i)):
            melhor = soma
            melhor_i = iTemp
            melhor_f = i
        n -= 1
        
    print("Teste "+ str(t))
    if (melhor == -1):
        print("nenhum\n")
    else:
        print("{} {}\n".format(str(melhor_i), str(melhor_f)))
    t += 1