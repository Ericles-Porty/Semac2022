while True:
  try:
    angulo = int(input())
    if angulo % 6 == 0:
      print("Y")
    else:
      print("N")
  except:
    break