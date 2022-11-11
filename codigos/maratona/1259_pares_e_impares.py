n = int(input())

pares = []
impares= []

for i in range(n):
  valor = int(input())
  if valor % 2 == 0:
    pares.append(valor)
  else:
    impares.append(valor)

pares.sort()
impares.sort(reverse = True)

for num in pares:
  print(num)

for num in impares:
  print(num)