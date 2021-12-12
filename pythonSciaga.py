# importowanie bibliotek
# from math import *
# # from math import sqrt
import math
import random
import enum

x = 20  # int
y = '20'  # string
z = True  # boolean
a = 4.20  # float

# zamiana na string
string = str(x)

# zamiana na int
intiger = int(y)

# komentarz w jednej lini

"""
Komentarz w 
kilku liniach
"""

# operatory w pythonie
# dodawanie/ odejmowanie
2 + 2
2-2
# mnozenie/ dzielenie / dzielenie bez reszty
2*2
2/2
10//3
# potęgowanie
4**2
# reszta z dzielenia
10 % 3
# pierwiastek z biblioteki math
print(math.sqrt(5))
# random z biblioteki random
random.randint(0, 100)

z = 1
z += 1  # z = z + 1
z *= 2  # z = z * 2
z /= 2  # z = z / 2

# https://docs.python.org/3/
# https://docs.python.org/3/library/functions.html


zmienna_z_dlugim_stringiem = """
    ale długi tekst normalnie
    az dwie linie owO
"""
print(zmienna_z_dlugim_stringiem)

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

""" Operatory logiczne
and - i
or - lub
not - negacja

"""
# pętla while
"""
while true:
    wykonaj kod

"""
num = 3

while num >= 0:
    print(num)
    num -= 1

i = 0
x = -5
while i < 10:
    # x = float(input('Podaj wartość: '))
    if (x < 0):
        print('miała być liczba większa od 0 zapytam ponownie')
    else:
        print(x)
    x = x + 1
    i += 1

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

for number in numbers:
    print(number)

if 'Kardiusz' in names:
    print('siema Kardiusz')

if 2 not in numbers:
    print('Nie ma liczby 2')

# listy metody
# len - długość
len(numbers)

#sum - suma
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
# uzywac jej za każdym razem kiedy wartośći w niej będą niezmienne
# zajmuje mniej miejsca w pamięci

krotka = (2, 4, 6, 8, 10)


# słownik(dictionary) - klucz i wartość

pokoje = {49: 'Jan Kowalski', 55: 'Ania Kowalska'}
pokoje[49]
pokoje.get(49)
pokoje[49] = 'Jan Nowak'
pokoje.update({56: 'Małgosia Nowak'})
print(pokoje)
del(pokoje[55])
pokoje.popitem()
pokoje.items()
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
    ('Mateusz', 18, 'mężczyzna')
    ('Jakub', 20, 'mężczyzna')
    ('Ania', 30, 'Kobirta')
]

listaGosci[0][0]

for imie, wiek, plec in listaGosci:
    print('Imie:', imie)
    print('Wiek:', wiek)
    print('Plec:', plec)

# słownik w liście
people = [
    {'id': 'IcFDG2bO9AYDF651DoyH', 'name': 'John', 'age': 27, 'sex': 'Male'},
    {'id': 'KcD9ntE6IRM59vkVta1k', 'name': 'Marie', 'age': 22, 'sex': 'Female'},
    {'id': 'yDlgcn99xPc19mYXcRmy', 'name': 'Agness', 'age': 25, 'sex': 'Female'},
    {'id': 'ABCgcn99xPc19mYXcRmy', 'name': 'Ann', 'age': 26, 'sex': 'Female'},
    {'id': 'DEFgcn667Pc19mYXcRmy', 'name': 'Peter', 'age': 30, 'sex': 'Male'},
    {'id': 'GHIgcn667Pc19mYXcRmy', 'name': 'Tony', 'age': 40, 'sex': 'Male'},
]

# słownik w słowniku
oceny = {
    {'name': 'John', 'age': 27, 'sex': 'Male'},
    {'name': 'Marie', 'age': 22, 'sex': 'Female'},
    {'name': 'Agness', 'age': 25, 'sex': 'Female'},
    {'name': 'Ann', 'age': 26, 'sex': 'Female'},
    {'name': 'Peter', 'age': 30, 'sex': 'Male'},
    {'name': 'Tony', 'age': 40, 'sex': 'Male'},
}

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
    "yDlgcn99xPc19mYXcRmy": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
    "cpQh6GiAbBdGv35NDoTk": {'name': 'Nabeel', 'age': 17, 'sex': 'Male'},
    "12BifzWxCQySKgLhgahC": {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
    "QLnmg0pzlLj9x7c7DlLv": {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
    "To47urX0DUznWmOxGZ6H": {'name': 'Lori', 'age': 27, 'sex': 'Male'},
    "KQ4bir3y4tlkbG69I7zq": {'name': 'Marie', 'age': 42, 'sex': 'Female'},
    "94cp4hsyZP2BnCh4D34z": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
    "Vr4wRdkljeEs46Czxo54": {'name': 'Chiara', 'age': 17, 'sex': 'Male'},
}

for key in people2:
    print('ID:', people2[key])
    for secondKey in people2[key]:
        print(secondKey, people2[key][secondKey])


# wyrażenia listowe
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

power = []
# for i in numbers:
#     power.append(i * i)
# print(power)

power = [i * i for i in numbers]

# wyrażenia generujące - nie czytują całej pamięci odrazu, oszczędzają zasoby
evenNumGen = (i for i in range(44000) if (i % 2 == 0))
for item in evenNumGen:
    print(item)

print(sum(evenNumGen))


# wyrażenia słownikowe
numbers = [1, 2, 3, 4, 5, 6]

multipliedNum = {
    number: number * number
    for number in numbers
}
celcius = {'t1': -8, 't2': -5, 't3': -6, 't4': -2, 't5': 4}
print(celcius)

farenheit = {
    key: celcius * 1.8 + 32
    for key, celcius in celcius.items()
}
print(farenheit)

# funkcje


def funkcja():
    print('kod w funkcji')


def wiadomosc(imie):
    print('cześć', imie)


imiona = ['Mateusz', 'Maciek', 'Bartek']

for imie in imiona:
    wiadomosc(imie)


# funckcje

Figury = enum.IntEnum(
    'menu_Figury', 'Kwadrat, Prostokąt, Koło, Trójkąt, Trapez')
wybor = int(input(""" wybierz figurę, której pole chcesz obliczyć:
1. Kwadrat
2. Prostokąt
3. Koło
4. Trójkąt
5. Trapez

"""))


def rectangle_surface(A, B):
    return A * B


def square_surface(A):
    return A**2


def triangle_surface(A, H):
    return(0.5*A*H)


def trapeze_surface(A, B, H):
    return((A+B) * 0.5 * H)


def circle_surface(R):
    return(R**2 * 3.14)


if(wybor == Figury.Kwadrat):
    A = float(input('Podaj bok kwadratu: '))
    square_surface(A)
elif(wybor == Figury.Prostokąt):
    A = float(input('Podaj bok A: '))
    B = float(input('Podaj bok B: '))
    rectangle_surface(A, B)


def suma_do(n):
    suma = 0
    for i in range(1, n + 1):
        suma = suma + i
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


# zasięg globalny i lokalny


def addl(y):
    # zasięg lokalny
    c = y
    print(c)


# zasięg globalny
c = 2


def addg():
    global c
    c = c + 3
    print(c)


# obiekty, zmienne to obiekty


a = 4
a.bit_length()

listSample = [1, 2, 3, 4, 5, 6]
listSample2 = listSample
listSample2.append(450)

# obie listy będą miały tą samą wartość

a = 4
b = a
b = 7


# a i b będą miały różne wartości

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
