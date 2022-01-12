"""
1. Jakiej długości ciąg wprowadził użytkownik?

2. Ile liter wchodzi w skład wprowadzonego ciągu?

3. Ile cyfr wchodzi w skład wprowadzonego ciągu?

4. Ile nie liter i nie cyfr wchodzi w skład wprowadzonego ciągu?

5. Ile wielkich liter wchodzi w skład?

6. Ile małych liter wchodzi w skład?

7. Jeżeli użytkownik wprowadził cyfry to jaką liczbę stworzą ustawione obok siebie w kolejności występowania w ciągu?

8. Jeżeli użytkownik wprowadził cyfry to sprawdź jaką wartość będzie miała ich suma z całego ciągu?

9. Czy w ciągu wprowadzonym znajduje się litera ‘a’, jeżeli tak to ile razy występuje?
"""

all_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
all_letters = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o',
               'ó', 'p', 'q', 'r', 's', 'ś', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ź', 'ż']
counted_digits = []


def len_of_string(characters):
    length_of_string = len(characters)
    return length_of_string


def how_many_letters(characters):
    counted_letters = [i for i in range(len(characters)) if characters[i].lower() in all_letters]
    return len(counted_letters)


def how_many_digits(characters):
    global counted_digits
    counted_digits = [characters[i] for i in range(len(characters)) if characters[i] in all_digits]
    return len(counted_digits)


def how_many_other_characters(characters):
    other_characters = []
    for i in range(len(characters)):
        if not characters[i].isnumeric() and not characters[i].isalpha():
            other_characters.append(i)
    return len(other_characters)


def how_many_big_letters(characters):
    big_letters = [all_letters[i].upper() for i in range(len(all_letters))]
    big_letters_in_input = [characters[i] for i in range(len(characters)) if characters[i] in big_letters]
    return len(big_letters_in_input)


def how_many_small_letters(characters):
    small_letters_in_input = [characters[i] for i in range(len(characters)) if characters[i] in all_letters]
    return len(small_letters_in_input)


def number_from_users_digits():
    number_from_users_input = ''
    for i in counted_digits:
        number_from_users_input += str(i)
    return number_from_users_input


def sum_of_users_digits():
    str_to_int = [int(counted_digits[i]) for i in range(len(counted_digits))]
    return sum(str_to_int)


def does_it_contain_a(characters):
    letters_a = [characters[i] for i in range(len(characters)) if characters[i].lower() in all_letters and characters[i].lower() == 'a']
    if len(letters_a) > 0:
        return f'9. w ciągu litera "A" znajduje się {len(letters_a)} razy'
    else:
        return 'nie ma litery A'


def main_program():
    # A!ABc@d217$1
    user_input = input('Podaj dowolny ciąg znaków: ')
    print(f'1. Ciąg ma długość {len_of_string(user_input)} znaków')
    print(f'2. Ciąg ma w sobie {how_many_letters(user_input)} liter')
    print(f'3. Ciąg ma w sobie {how_many_digits(user_input)} cyfr')
    print(f'4. Ciąg ma w sobie {how_many_other_characters(user_input)} pozostałych znaków')
    print(f'5. Ciąg ma w sobie {how_many_big_letters(user_input)} wielkich liter')
    print(f'6. Ciąg ma w sobie {how_many_small_letters(user_input)} małych liter')
    print(f'7. Wprowadzone przez użytkownika cyfry utworzą liczbę: {number_from_users_digits()}')
    print(f'8. Suma z całego ciągu cyfr wprowadzonych przez użytkownika to: {sum_of_users_digits()}')
    print(does_it_contain_a(user_input))


main_program()