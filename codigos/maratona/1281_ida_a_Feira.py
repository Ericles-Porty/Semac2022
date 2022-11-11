casos = int(input())

for i in range(casos):
  totalItens = int(input())
  items = []
  valores = []
  for a in range(totalItens):
    item, valor = input().split()
    valor = float(valor)
    items.append(item)
    valores.append(valor)    

  totalItensAComprar = int(input())
  itemsAComprar = []
  quantidade = []
  for b in range(totalItensAComprar):
    item, qtde = input().split()
    qtde = int(qtde)
    itemsAComprar.append(item)
    quantidade.append(qtde)

  total = 0
  for i in range(len(itemsAComprar)):
    try:
      index = items.index(itemsAComprar[i])
      total = total + (quantidade[i] * valores[index])
    except:
      continue

  print("R$ {0:.2f}".format(total))
      
