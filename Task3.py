
x = int(input('x = '))
y = int(input('y = '))
A = (x,y)
print(f'A {A}')

if x > 0 and y > 0:
    print('Первая четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
else:
     print('Решения нет')
    