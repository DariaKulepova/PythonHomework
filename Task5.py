import math
x = float(input('x = '))
y = float(input('y = '))
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

print(f'A{x,y}; B{x2,y2}')

d = math.sqrt((x2-x)**2 + (y2-y)**2)
print (round(d,2))
