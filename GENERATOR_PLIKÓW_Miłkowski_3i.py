"""
Zadanie 1 Stwórz program generujący plik zwierający w każdej linijce ciąg znaków:

1. Stwórz listę lub krotkę zawierającą litery A-Z, a-z i cyfry 0-9. Mogą być ze sobą pomieszane istotne żeby były
wszystkie. Jeżeli będzie ci łatwiej podzielić znaki na więcej tablic i z nich losować to śmiało.

2. Generator losuje ilość wierszy z przedziału <50, 300>.

3. Tworzy plik i w każdy wiersz wstawia ciąg znaków o losowej długości od 3 do 20 znaków. Znaki losowane są z kontenera
stworzonego w punkcie pierwszym.

4. Odczytaj plik i wyświetl jego zawartość w konsoli.

Zadanie2 Zmodyfikuj kod z Zadania 6 2021 tak, by mógł przeanalizować ciągi znaków z pliku stworzonego przez twój
generator
"""

# zadanie 1
import random

chars = [chr(i) for i in range(97, 123)]
chars += [chr(i) for i in range(65, 91)]
chars += [str(i) for i in range(10)]


def writing(num_of_lines):
    with open('text', 'w', encoding='UTF-8') as file:
        for line in range(num_of_lines):
            len_of_line = random.randint(3, 20)
            for i in range(len_of_line):
                rand_char = chars[random.randint(0, len(chars) - 1)]
                file.write(rand_char)
            file.write('\n')


def reading(file_name):
    with open(file_name, 'r', encoding='UTF-8') as file:
        for line in file:
            print(line)


def main_func():
    num_of_lines = random.randint(50, 300)
    writing(num_of_lines)
    reading('text')


# zadanie 2
all_digits = [str(i) for i in range(10)]
all_letters = [chr(i) for i in range(97, 123)]


def len_of_string(characters):
    length_of_string = len(characters)
    return f'1. Ciąg ma długość {length_of_string} znaków'


def how_many_letters(characters):
    counted_letters = [i for i in range(len(characters)) if characters[i].lower() in all_letters]
    return f'2. Ciąg ma w sobie {len(counted_letters)} liter'


def how_many_digits(characters):
    counted_digits = [characters[i] for i in range(len(characters)) if characters[i] in all_digits]
    return f'3. Ciąg ma w sobie {len(counted_digits)} cyfr'


def how_many_other_characters(characters):
    other_characters = []
    for i in range(len(characters)):
        if not characters[i].isnumeric() and not characters[i].isalpha() and not '\n':
            other_characters.append(characters[i])
    return f'4. Ciąg ma w sobie {len(other_characters)} pozostałych znaków'


def how_many_big_letters(characters):
    big_letters = [all_letters[i].upper() for i in range(len(all_letters))]
    big_letters_in_input = [characters[i] for i in range(len(characters)) if characters[i] in big_letters]
    return f'5. Ciąg ma w sobie {len(big_letters_in_input)} wielkich liter'


def how_many_small_letters(characters):
    small_letters_in_input = [characters[i] for i in range(len(characters)) if characters[i] in all_letters]
    return f'6. Ciąg ma w sobie {len(small_letters_in_input)} małych liter'


def number_from_users_digits(characters):
    counted_digits = [characters[i] for i in range(len(characters)) if characters[i] in all_digits]
    number_from_users_input = ''
    for i in counted_digits:
        number_from_users_input += str(i)
    return f'7. Wprowadzone przez użytkownika cyfry utworzą liczbę: {number_from_users_input}'


def sum_of_users_digits(characters):
    counted_digits = [characters[i] for i in range(len(characters)) if characters[i] in all_digits]
    str_to_int = [int(counted_digits[i]) for i in range(len(counted_digits))]
    return f'8. Wprowadzone przez użytkownika sumują się do: {sum(str_to_int)}'


def does_it_contain_a(characters):
    letters_a = [characters[i] for i in range(len(characters)) if
                 characters[i].lower() in all_letters and characters[i].lower() == 'a']
    if len(letters_a) > 0:
        return f'9. W ciągu litera "A" znajduje się {len(letters_a)} razy'
    else:
        return '9. Nie ma litery A'


def string_info(*functions):
    with open('text') as file:
        for line in file:
            print(line)
            for function in functions:
                print(function(line))
            print('\n')


string_info(len_of_string, how_many_letters, how_many_digits, how_many_other_characters,
            how_many_big_letters, how_many_small_letters, number_from_users_digits, sum_of_users_digits,
            does_it_contain_a, )
