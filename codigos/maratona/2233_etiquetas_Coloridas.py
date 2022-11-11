r = int(input(), 16)
g = int(input(), 16)
b = int(input(), 16)

totalR = 1
totalG = 0
totalB = 0

totalG = r // g
totalG *= totalG

totalB = g // b
totalB *= totalB
totalB *= totalG

print('{:x}'.format(totalR + totalG + totalB))