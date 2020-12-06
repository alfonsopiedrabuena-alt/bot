#es una buena practica dejar dos espacios(renglón) entre cada función
def palindromo(palabra):
    palabra = palabra.replace(' ','')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False

#es necesario correr esta funcion como principal a diferencia de C se usa run aunque puedes usar Main si así lo deseas
def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == "__main__":
    run()