nombre_1 = input('¿cómo se llama la persona 1: ')
edad_1 = int(input('¿qué edad tiene la persona 1? '))
nombre_2 = input('¿cómo se llama la persona 2: ')
edad_2 = int(input('¿qué edad tiene la persona 2? '))

if edad_1 > edad_2:
    print(f'{nombre_1} es mayor que {nombre_2} ya que tiene {edad_1}, mientras que {nombre_2} tiene {edad_2}, se llevan por lo menos: ')
elif edad_1 < edad_2:
    print(f'{nombre_1} es menor que {nombre_2} ya que tiene {edad_1}, mientras que {nombre_2} tiene {edad_2}')
else:
    print('todos tienen la misma edad que tonteria')