import pprint
import math
import random
import enum
import time
import json
import requests
from collections import Counter
import collections
import webbrowser
from datetime import datetime, timedelta

"""
skróty klawiszowe
shift + f6 = zmiana nazwy zmiennej
ctrl + shift + strzałki = przeniesienie kodu
ctrl + alt + l = upiększanie kodu
"""

"""
funkcje - z małej

"""
# importowanie bibliotek
# PyPI


y = 20
f'string{y} ze zmienna'

# dzielenie bez reszty
print(10 // 3)
# potęgowanie
print(4 ** 2)
# reszta z dzielenia
print(10 % 3)
# pierwiastek z biblioteki math
print(math.sqrt(5))
# random z biblioteki random
random.randint(0, 100)  # od 0 do 100
random.randrange(10)  # od 0 do 99
random.randrange(0, 16, 2)  # przeskakuje co 2

# https://docs.python.org/3/
# https://docs.python.org/3/library/functions.html


zmienna_z_dlugim_stringiem = """
    ale długi tekst normalnie
    az dwie linie owO
"""

imie = "mateusz"
print(imie[0])
print(imie[-1])
print(imie[0:3])

imie_z_duzej = imie.capitalize()
imieCaps = imie.upper()
imieSmol = imie.lower()

""" operatory porównania
< - mniejsze od
> - większe od
= - operator przypisania
== - równe
=== - równe z typem
! - rózne
"""

# pętla while
num = 3

while num >= 0:
    print(num)
    num -= 1

# pętla for
for i in range(6):
    print(i)

# brak, zakończy program gdy dojdzie do break
number = random.randint(0, 100)

while True:
    userInput = int(input('zgadnij liczbę: '))
    if userInput == number:
        print('wygrałeś')
        break
    elif userInput < number:
        print('twoja liczba jest za mała')
    else:
        print('twoja liczba jest za duża')
print('koniec gry')

# continue, przerywamy ale mozemy kontynuowac
wynik = 0
for i in range(9):
    if i == 3:
        print('i = 3')
        continue
    print(i)

"""                         el.unikalne     kolejność   zmiana konkretnego el.  nowe el
 listy[]                      nie             tak         tak                     tak
 krotki()                     nie             tak         nie                     nie

 słowniki{'klucz': wartość}   tak             nie         tak                     nie
 zbiory{}                     tak             nie         nie                     tak
"""
# listy
lista = []
names = ['Mateusz', 'Kardiusz', 'Wioletta', 'Kuba', 'Arkadiusz']
numbers = [2137, 420, 69, 69, 1410]

# listy metody
# len - długość
len(numbers)

# sum - suma
sum(numbers)

# append dodac na koncu
numbers.append(12)

# extend - rozszerzyc
numbers.extend([1, 2, 3])

# insert - dodac na podanym indeksie
numbers.insert(0, [9, 8, 7])

# index - podajemy jakąś wartość i dostajemy jej indeks
names.index('Mateusz')

# sort sortuje liste, modyfikując ją
numbers.sort()
numbers.sort(reverse=True)

# max - max wartość
max(numbers)

# min - min wartość
min(numbers)

# count - ile razy wystąpiło
numbers.count(69)

# pop - usuwanie ostatniego elementu
numbers.pop()

# remove - usuwanie 1 napotkanego elementu
numbers.remove(69)

# clear - czyszczenie listy
names.clear()

# reverse
numbers.reverse()

# krotka(TUPLA)- lista której nie da się edytować
krotka = (2, 4, 6, 8, 10)

# słownik(dictionary) - klucz i wartość
pokoje = {49: 'Jan Kowalski', 55: 'Ania Kowalska'}

# zbiory - są unikalne

zbior1 = {1, 4, 20, -4}
zbior2 = {1, 5, 20, -8}
# wspólne lementy zbiorów
print(zbior1 & zbior2)
# suma elementów zbioru ale z unikalnymi elementami
print(zbior1 | zbior2)
# tylko unikalne wartości
print(zbior1 - zbior2)
# usuwanie
zbior1.discard(1)
# czy jeden zbiór jest podzbiorem drugiego
print(zbior1.issubset(zbior2))

# zagnieżdżanie typów danych

listaGosci = [
    ('Mateusz', 18, 'mężczyzna'),
    ('Jakub', 20, 'mężczyzna'),
    ('Ania', 30, 'Kobirta')
]

print(listaGosci[0][0])

for imie, wiek, plec in listaGosci:
    print('Imie:', imie)
    print('Wiek:', wiek)
    print('Plec:', plec)

# zbiór
ratings = {
    'Arkadiusz': (2, 1, 3, 4, 5, 6),
    'Agnes': (2, 1, 3, 4, 5, 6)
}

# wypiwyswanie wartości słownika zagnieżdonego w liście/ słowniku
for key in ratings:
    print(key, 'oceny: ', ratings[key])

people2 = {
    "IcFDG2bO9AYDF651DoyH": {'name': 'John', 'age': 27, 'sex': 'Male'},
    "KcD9ntE6IRM59vkVta1k": {'name': 'Marie', 'age': 22, 'sex': 'Female'},
    "yDlgcn99xPc19mYXcRmy": {'name': 'Agness', 'age': 25, 'sex': 'Female'}
}

for key in people2:
    print('ID:', people2[key])
    for secondKey in people2[key]:
        print(secondKey, people2[key][secondKey])

# wyrażenia listowe
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

power = [i * i for i in numbers]

# wyrażenia generujące - nie czytują całej pamięci odrazu, oszczędzają zasoby
evenNumGen = (i for i in range(44000) if (i % 2 == 0))
for item in evenNumGen:
    print(item)

print(sum(evenNumGen))

# wyrażenia słownikowe
celcius = {'t1': -8, 't2': -5, 't3': -6, 't4': -2, 't5': 4}

farenheit = {
    key: celcius * 1.8 + 32
    for key, celcius in celcius.items()
}

# funckcje

Figury = enum.IntEnum(
    'menu_Figury', 'Kwadrat, Prostokąt, Koło, Trójkąt, Trapez')


def rectangle_surface(a, b):
    return a * b


# funkcje anonimowe lambda
print((lambda x: x * 2)(4))


# wydajność kodu
def function_performance(func):
    start = time.perf_counter()
    func()
    stop = time.perf_counter()
    print(stop - start)


# argumenty kluczowe i pozycyjne
def greet(name, message, separator=''):
    print(message, name, separator)


greet('mateusz', 'siema', '\n')

# argument wielowartościowy
"""
*arg - deklaracja argumentu wielowartościowego, 
od tego momentu możemy przesłać więcej niż jeden argument nienazwany. 
Automatycznie po przesłaniu argumentu jest on krotką.
"""


def suma(*numbers):
    result = 0
    for i in range(len(numbers)):
        result += numbers[i]
    print(result)


suma(2, 4, 1, 2, 4, 5, 10)

"""
** arg - argument wielowartościowy, nazwany który może przyjmować klucze - wartości. 
Ostatecznie argumenty po przesłaniu będą słownikiem.
"""


# kopiowanie elementów, kopia płytka


def delete_func(list):
    list.clear()


myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

delete_func(myList.copy())

# zdarzenia losowe
hit_list = []


def coin_flip():
    flip = random.randint(0, 100)
    if flip > 50:
        return 'orzeł'
    else:
        return 'reszka'


for i in range(101):
    hit_list.append(coin_flip())

dictionaryHit = Counter(hit_list)

# choice i choices
# choice równy % na wylosowanie
type_of_loot = ['basic', 'magic', 'epic', 'legendary']
print(random.choice(type_of_loot))

# choices
random.choices(type_of_loot, [1, 0.5, 0.25, 0.1], k=100)
print(Counter(random.choices(type_of_loot, [1, 0.5, 0.25, 0.01], k=1000)))

# shufle

cardList = ['9', '9', '9', '9', '10', '10', '10', '10', 'jack', 'jack', 'jack', 'jack', 'Queen', 'Queen', 'Queen',
            'Queen', ]
random.shuffle(cardList)


# losowanie unikalncyh liczb (sample)

def lotto(how_many_numbers, range_num):
    print(random.sample(range(range_num + 1), how_many_numbers))


# praca na plikach
"""
r - R ead (czytanie) - domyślne
w - W rite (pisanie) - jeżeli plik istnieje to go usunie, jeżeli nie istnieje to go utworzy
a - Append (dopisywanie)
r+ - służy do pisania i odczytywanua

operacje
1)otwieranie
2)pisanie/czytanie
3)zamykanie
"""

file = open('plik_tekstowy', 'w')
file.write('sample')
file.close()

# try i finally
try:
    file = open('plik_tekstowy', 'w')
    file.write('sample')
finally:
    file.close()

with open('plik_tekstowy', 'w', encoding='UTF-8') as file2:
    file2.write('dick')

"""
read
readline
readlines
splitlines

"""

with open('plik_tekstowy', 'r', encoding='UTF-8') as file3:
    x = file.read().splitlines()

"""
tell - mówi gdzie skończyliśmy operacje na pliku
seek - szuka (zmienia) - miejsce odczyty zapisu na wskazane prez nas
"""
with open('plik_tekstowy', 'r', encoding='UTF-8') as file4:
    print(file.tell())

# dopisywanie
with open('plik_tekstowy', 'a', encoding='UTF-8') as file5:
    print(file.write('dopisane'))

"""
r+ - czytanie i pisanie
w+
a+
"""
# cwiczenie


namesAndSurnames = []

with open('imionanazwiska.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        namesAndSurnames.append(tuple(line.replace('\n', "").split(" ")))

with open('imiona.txt', 'w', encoding='UTF-8') as file:
    for item in namesAndSurnames:
        try:
            file.write(item[0] + '\n')
        except IndexError:
            file.write('\n')

"""
JSON
trzeba zaimportować bibliotekę json
"""

# json.dump(data) - zapisuje dane do postaci Stringowej
# json.dump(data, nameOfFileHandler, ensure_ascii=False) - zapisuje do json

film = {
    "title": 'Zjawa',
    'genre': 'drama',
    'release_year': 2016,
    'length(min)': 156,
    'main_actor': 'Leonardo Dicaprio',
    'won_oscar': True,
}

with open('sample.json', 'w', encoding='UTF-8') as file:
    json.dump(film, file, ensure_ascii=False)

# odczytywanie json
odczytanyJson = json.dumps(film, ensure_ascii=False, indent=4)

with open('sample.json', encoding='UTF-8') as file6:
    wynik = json.load(file6)

print(odczytanyJson)

# PyPi i instalacja zewnętrznych pakunków REQUEST
"""
Instalacja:
1.odpalic CMD w folderze w którym jest python 
2. Wpisać komende: python -m pip install [nazwa_paczki]

"""
response = requests.get('https://videokurs.pl')


# sprawdz czy strony odpowiadają


def which_page_works():
    with open('stronki.txt') as file:
        pages = [line.replace('\n', '') for line in file]
    for link in range(len(pages)):
        print(pages[link])
        try:
            response = requests.get(pages[link])
            if response.status_code == 200:
                print('działa')
        except requests.exceptions.RequestException:
            print('nie działa')


which_page_works()


# pobieranie danych z serwera
# przydatna strona: https://jsonplaceholder.typicode.com


def find_best_users(dict_of_stats):
    max_amount_of_tasks = max(dict_of_stats)
    best_users = []
    for stat in dict_of_stats:
        if stat == max_amount_of_tasks:
            best_users.append(stat)
    return best_users


def give_award_to_best_employee(json_file):
    tasks = json_file.json()
    num_of_completed_tasks_by_user = collections.defaultdict(int)
    for task in tasks:
        if task['completed']:
            num_of_completed_tasks_by_user[task['userId']] += 1
    print(find_best_users(num_of_completed_tasks_by_user.items()))


list_of_workers = requests.get("https://jsonplaceholder.typicode.com/todos")
give_award_to_best_employee(list_of_workers)

list_of_workers = requests.get("https://jsonplaceholder.typicode.com/todos")

"""
API - aplication programing interface
"""
time_before = timedelta(days=3)
search_date = datetime.today() - time_before

params = {
    'site': 'stackoveflow',
    'sort': 'votes',
    'order': 'desc',
    'fromdate': int(search_date.timestamp()),
    'tagged': 'python',
    # 'min': 15
}

r = requests.get("https://api.stackexchange.com/2.2/questions/", params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print('niepoprawny format')
else:
    for question in questions:
        pprint.pprint(question['link'])
        webbrowser.open_new_tab(question['link'])

    # POST i DELETE

    # calendarific.com

headers = {
    "x-api-key": 'tu podaj swój API_key'
}

r = requests.get('https://api.thecatapi.com/vl/favourites', headers=headers)

"""
funkcje generujące
"""
def generate_10_num()
    x = 0
    while x < 10:
        yield x
        x += 1

next(generate_10_num())
"""
stwórz funkcję generującą x * x tj 1*1, 2*2, 3*3
"""

def num_multiply_by_itself():
    number = 0
    while True:
        number = number + 1
        yield number

next(num_multiply_by_itself())