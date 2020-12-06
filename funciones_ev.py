def run():
    print(""" 
    ¡Hola! a continuación deberás de elegir entre las siguientes tres opciones:
    1) Enumeración exhaustiva
    2) Aproximación de solución
    3) Búsqueda binaria
    Posterior te pediremos que incluyas el número sobre el cual quieres obtener
    la raíz cuadrada.
    """)
    opcion = int(input('¿qué opción quieres tomar?: '))
    objetivo = int(input('¿Sobre que número deseas correr el ejercicio para obtener la razí cuadrada?: '))

    if opcion == 1:
        print('Seleccionaste la opción número 1, Enumeración Exhaustiva')
        enumeracion_ex(objetivo)
        return True
    elif opcion == 2:
        print('Seleccionaste la opción número 2, Aproximación de Solución')
        aprox_sol(objetivo)
        return True
    else:
        print('Seleccionaste la opción número 3, Búsqueda Binaria')
        busq_bin(objetivo)
        return True



def enumeracion_ex(objetivo):
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'La raíz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raíz cuadrada exacta')


def aprox_sol(objetivo):
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontró la raíz cuadrada {objetivo}')
    else:
        print(f'La raíz cuadrada de {objetivo} es {respuesta}')


def busq_bin(objetivo):
    epsilon = 0.01
    bajo = 0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        
        respuesta = (alto + bajo) / 2

    print(f'La raíz cuadrada de {objetivo} es {respuesta}')
    

if __name__ == '__main__':
    run()