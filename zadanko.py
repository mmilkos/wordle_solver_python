import random

chars = [chr(i) for i in range(97, 123)]
chars += [chr(i) for i in range(65, 91)]
chars += [str(i) for i in range(10)]


def reading(file_name):
    with open(file_name, 'r', encoding='UTF-8') as file:
        for line in file:
            print(line)


def writing(num_of_lines):
    with open('text', 'w', encoding='UTF-8') as file:
        for line in range(num_of_lines):
            len_of_line = random.randint(3, 20)
            for i in range(len_of_line):
                rand_char = chars[random.randint(0, len(chars) - 1)]
                file.write(rand_char)
            file.write('\n')


def main_func():
    num_of_lines = random.randint(50, 300)
    writing(num_of_lines)
    reading('text')


main_func()
