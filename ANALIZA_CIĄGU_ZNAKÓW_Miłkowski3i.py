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
        if not characters[i].isnumeric() and not characters[i].isalpha():
            other_characters.append(i)
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
    return f'8. Wprowadzone przez użytkownika cyfry utworzą liczbę: {sum(str_to_int)}'


def does_it_contain_a(characters):
    letters_a = [characters[i] for i in range(len(characters)) if characters[i].lower() in all_letters and characters[i].lower() == 'a']
    if len(letters_a) > 0:
        return f'9. w ciągu litera "A" znajduje się {len(letters_a)} razy'
    else:
        return 'nie ma litery A'


def string_info(*functions):
    # A!ABc@d245$4a
    user_input = input('Podaj dowolny ciąg znaków: ')
    for function in functions:
        print(function(user_input))


string_info(len_of_string, how_many_letters, how_many_digits,how_many_other_characters,
             how_many_big_letters, how_many_small_letters, number_from_users_digits, sum_of_users_digits,
             does_it_contain_a,)