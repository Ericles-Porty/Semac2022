while True:
  try:
    s = input()
    if s == "1 0 0" or s == "0 1 1":
      print("A")
    elif s == "0 1 0" or s == "1 0 1":
      print("B")
    elif s == "0 0 1" or s == "1 1 0":
      print("C")
    else:
      print("*")
  except:
    break