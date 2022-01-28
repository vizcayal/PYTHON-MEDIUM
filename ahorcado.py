from constants import *
import random
import os

def file_list(file_name):
    words = []
    file = open(file_name, "r", encoding= "utf-8")
    for line in file:
            words.append(line.strip())
    file.close()
    
    return words


def run():
    os.system("cls")

    i = 0
    Letras = []
    word_list = file_list('data.txt')
    random_number = random.randint(0, len(word_list) - 1)
    word = word_list[random_number]
    gano = False
    while (i < TRIES) and (not gano):
        Letra = input("Ingrese una Letra: ")
        if not(Letra in Letras):
            Letras.append(Letra)
        if not(Letra in word):
            i+=1
        
        os.system("cls")

        a = list(filter(lambda l:l in Letras,word))
        print(a)
        
        print("te quedan {} intentos".format(TRIES - i))
        if len(a) == len(word):
            gano = True
            print("Ganaste...")

        print("\n")
        
        
    print('La palabra es: ', word)

if __name__ == '__main__':
    run()