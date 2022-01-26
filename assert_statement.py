def divisores(num):
    divisor = []
    for i in range(1,num+1):
        if num % i == 0:
            divisor.append(i)
    return divisor

def run():
    num = input("Ingrese Numero")
    assert num.isnumeric(), "Ingrese un numero"
    d = divisores(num)
    print(d)
    print('Termino mi programa')

if __name__ == '__main__':
    run()
    
