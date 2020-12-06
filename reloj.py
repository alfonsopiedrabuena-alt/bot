horas = 00
minutos = 00
segundos = 00

while horas < 12:
    while minutos < 30:
        while segundos < 20:
            print(horas, minutos, segundos)
            segundos += 1

            if segundos == 60:
                break

        minutos += 1
        segundos = 0

        if minutos == 60:
            break

    horas += 1
    minutos = 0
    segundos = 0



