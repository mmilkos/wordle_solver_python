# dodanie GUI przycisków kalkulatora, wynik jest podawany w konsoli

from tkinter import *

# tkinter
root = Tk()
root.title('Kalkulator')


# przyciski z liczbami
number = 9
r = 4
c = 3
for row in range(1, r):
    for col in range(0, c):
        button = Button(root, text=number, padx="40", pady="20")
        button.grid(row=row + 2, column=c - col)
        button['command'] = lambda btn = button: button_add(btn)
        number -= 1

button0 = Button(root, text='0', padx="39", pady="19",)
button0['command'] = lambda btn = button0: button_add(btn)
button0.grid(row=row + 3, column=c - col +1)


# inicjowanie zmiennych
first_num = ""
second_num = ""
isButtonClicked = False
first_container = []
second_container = []
type_of_operation = []


# przyciski funkcyjne
# plus
buttonPlus = Button(root, text='+', padx="39", pady="19",)
buttonPlus['command'] = lambda plus = buttonPlus: plusClick(plus)
buttonPlus.grid(row=row + 4, column=c - col)

# minus
buttonMinus = Button(root, text='-', padx="41", pady="19")
buttonMinus.grid(row=row + 4, column=c - col + 1)
buttonMinus['command'] = lambda minus = buttonMinus: minusClick(minus)

# razy
buttonMultiply = Button(root, text='*', padx="40", pady="20")
buttonMultiply.grid(row=row + 4, column=c - col + 2)
buttonMultiply['command'] = lambda mult = buttonMultiply: multiplyClick(mult)

# podzielić
buttonDivide = Button(root, text=':', padx="41", pady="20")
buttonDivide.grid(row=row + 5, column=c - col)
buttonDivide['command'] = lambda divide = buttonDivide: divideClick(divide)

# równa się
buttonEquals = Button(root, text='=', padx="39",
                      pady="20", command=lambda: equals())
buttonEquals.grid(row=row + 5, column=c - col + 1, )

# czyszczenie
buttonClear = Button(root, text='C', padx="39",
                     pady="20", command=lambda: clear())
buttonClear.grid(row=row + 5, column=c - col + 2)


# funkcje przekazujące typ działania
def plusClick(plus):
    global isButtonClicked
    isButtonClicked = True
    print(first_num)
    print(str(plus['text']))
    type_of_operation.append(str(plus['text']))


def minusClick(minus):
    global isButtonClicked
    isButtonClicked = True
    print(first_num)
    print(str(minus['text']))
    type_of_operation.append(str(minus['text']))


def multiplyClick(mult):
    global isButtonClicked
    isButtonClicked = True
    print(first_num)
    print(str(mult['text']))
    type_of_operation.append(str(mult['text']))


def divideClick(mult):
    global isButtonClicked
    isButtonClicked = True
    print(first_num)
    print(str(mult['text']))
    type_of_operation.append(str(mult['text']))


# funkcja czyszcząca pamięć
def clear():
    global isButtonClicked
    global first_num
    global second_num
    global first_container
    global second_container
    global type_of_operation
    isButtonClicked = False
    first_container = []
    second_container = []
    type_of_operation = []
    second_num = ""
    first_num = ""


# funkcja tworząca liczby
def button_add(but):
    global first_num
    global second_num
    if not isButtonClicked:
        first_container.append(str(but['text']))
        first_num = ("".join(first_container))
    else:
        second_container.append(str(but['text']))
        second_num = ("".join(second_container))

# kalkulator


# funkcja odpowiedzialna za dodawanie
def suma(a, b):
    return print(a + b)


# funkcja odpowiedzialna za odejmowanie
def roznica(a, b):
    return print(a - b)


# funkcja odpowiedzialna za mnożenie
def iloczyn(a, b):
    return print(a * b)


# funkcja odpowiedzialna za dzielenie
def iloraz(a, b):
    return print(a/b)


# funkcja odpowiadająca za podawanie wyników
def equals():
    if '+' in type_of_operation:
        print(second_num)
        print('=')
        suma(int(first_num), int(second_num))
    elif '-' in type_of_operation:
        print(second_num)
        print('=')
        roznica(int(first_num), int(second_num))
    elif '*' in type_of_operation:
        print(second_num)
        print('=')
        iloczyn(int(first_num), int(second_num))
    elif ':' in type_of_operation:
        print(second_num)
        print('=')
        iloraz(int(first_num), int(second_num))
    clear()


root.mainloop()
