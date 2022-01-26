def divisores(num):
    divisor = []
    for i in range(1,num+1):
        if num % i == 0:
            divisor.append(i)
    return divisor

def run():
    try:
        num = int(input("Ingrese Numero"))
        if num<=0:
            raise ValueError
        d = divisores(num)
        print(d)
        print('Termino mi programa')
    except ValueError:
        print('Ingrese solo numeros positivos')

if __name__ == '__main__':
    run()
    
