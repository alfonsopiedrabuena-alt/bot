def run():
#    for contador in range(0,1000):
#        if contador % 3 != 0:
#            continue
#        print(contador)


#    for i in range (10000):
#         print (i)
#         if i ==5678:
#             break

#   texto = input('Escribe un texto: ')
#   for letra in texto:
#       if letra == 'o':
#           break
#       print(letra)

    numero = 1
    while numero <= 300:
        numero = 3 * numero + 1
        if numero == 364:
            break
        print(numero)

if __name__ == '__main__':
    run()