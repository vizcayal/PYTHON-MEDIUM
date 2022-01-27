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
    i = 0
    Letras = []
    word_list = file_list('data.txt')
    random_number = random.randint(0, len(word_list) - 1)
    word = word_list[random_number]
    while i < TRIES+10:
        Letra = input("Ingrese una Letra: ")
        Letras.append(Letra)
        i=i+1
        os.system("cls")
        print([l for l in word if l in Letras])
        
        
    print('La palabra es: ', word)

if __name__ == '__main__':
    run()