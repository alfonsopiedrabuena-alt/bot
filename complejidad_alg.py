import time

def factorial(n):
    respuesta = 1
    
    while n > 1:
        respuesta *= n
        n -= 1
        
    return respuesta

def factorial_r(n):
    if n == 1:
        return 1
    return n * factorial (n-1)

if __name__ == '__main__':
    n = 200000
#no llega a más de     
    comienzo = time.time()
    # demasiados datos impresos: print(factorial(n))
    factorial(n)
    final = time.time()
    print(final-comienzo)
    
    comienzo = time.time()
    #lo mismo imprime demasiado datos para lo que se esta buscando print(factorial_r(n))
    factorial_r(n)
    final = time.time()
    print(final-comienzo)