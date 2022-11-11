def inverteValor(v):
  resp = v[1] + v[0]
  return resp

n, m = map(int,input().split())

matrix = []

for i in range(n):
  valores = [x for x in input().split()]
  for j in range(m):
    valor = inverteValor(valores[j]) 
    matrix.append(valor)

matrix.sort(reverse = True)

for i in range(len(matrix)):
  print(inverteValor(matrix[i]))