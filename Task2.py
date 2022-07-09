x = int(input('Введите 0 или 1 x = '))
y = int(input('Введите 0 или 1 y = '))
z = int(input('Введите 0 или 1 z = '))



def check_statement (x, y, z):
   
       return (not (x or y or z)) == (not x and not y and not z)
if 0 <=x <= 1 and 0 <=y <= 1 and 0 <=z <= 1 :
    
     print(f'¬({x} V {y} V {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z}) is {(not (x or y or z)) == (not x and not y and not z)}')
else:
      print("Ложно")
  
    
    