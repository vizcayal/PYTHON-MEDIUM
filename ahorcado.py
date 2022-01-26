def file_list(file_name):
    words = []
    file = open(file_name, "r", encoding= "utf-8")
    for line in file:
            words.append(line.strip())
    file.close()
    return words


def run():
    word_list = file_list('data.txt')
    random_number = random.randint(0, len(word_list) - 1)
    word = word_list[random_number]
    

if __name__ == '__main__':
    run()