n = int(input())

bobo = int(input())
resp = "S"
for i in range(n - 1):
  votos = int(input())
  if votos > bobo:
    resp = "N"
print(resp)