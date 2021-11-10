"""
Po podaniu dwóch liczb (num1 i num2) i wybraniu działania('+' - dodawanie, '-' - odejmowanie, '*' - mnożenie,
':' - dzielenie) kalkulator przeprowadza te działanie na podanych liczbach
"""

# Input użytkownika
num1 = float(input("Podaj liczbę 1:"))
num2 = float(input("Podaj liczbę 2:"))
rodzaj = str(input("Podaj typ działania (+,-,*,:):"))

# funkcja dodawania dodaje num1 i num2
def dodawanie(num1, num2):
    print(num1 + num2)

# funkcja odejmowania odejmuje num2 od num1
def odejmowanie(num1, num2):
    print(num1 - num2)

# funkcja mnożenia mnoży num1 przez num2
def mnozenie(num1, num2):
    print(num1 * num2)

# funkcja dzielenie dzieli num1 przez num2
def dzielenie(num1, num2):
    print(num1 / num2)

# funkcja wynik podaje wynik w zależności od wybranego działania
def wynik():
    if rodzaj == '+':
        dodawanie(num1, num2)
    elif rodzaj == '-':
        odejmowanie(num1, num2)
    elif rodzaj == '*':
        mnozenie(num1, num2)
    elif rodzaj == ':':
        dzielenie(num1, num2)

# wywołanie funkcji wynik
wynik()