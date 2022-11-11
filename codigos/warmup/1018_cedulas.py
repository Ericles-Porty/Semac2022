valor = int(input())

print(valor)

notas100 = int(valor / 100)
valor = valor - notas100 * 100

notas50 = int(valor / 50)
valor = valor - notas50 * 50

notas20 = int(valor / 20)
valor = valor - notas20 * 20

notas10 = int(valor / 10)
valor = valor - notas10 * 10

notas5 = int(valor / 5)
valor = valor - notas5 * 5

notas2 = int(valor / 2)
valor = valor - notas2 * 2

notas1 = int(valor / 1)
valor = valor - notas1 * 1

print("{0} nota(s) de R$ 100,00".format(notas100))
print("{0} nota(s) de R$ 50,00".format(notas50))
print("{0} nota(s) de R$ 20,00".format(notas20))
print("{0} nota(s) de R$ 10,00".format(notas10))
print("{0} nota(s) de R$ 5,00".format(notas5))
print("{0} nota(s) de R$ 2,00".format(notas2))
print("{0} nota(s) de R$ 1,00".format(notas1))