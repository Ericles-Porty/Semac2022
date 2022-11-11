
def extrairVogais(risada):
    vogais = ['a', 'e', 'i', 'o', 'u']
    risadaDeVogais = ""
    for letra in risada:
        if (letra in vogais):
            risadaDeVogais += letra
    return risadaDeVogais

def inverter(txt):
  return txt[::-1]

original = input()
sohVogais = extrairVogais(original)
if (sohVogais == inverter(sohVogais)):
    print("S")
else:
    print("N")