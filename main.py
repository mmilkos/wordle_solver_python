from tkinter import *

root = Tk()

numbers = []

#funkcje kalkulatora


def dodawanie(a, b):
    return a + b


def odejmowanie(a, b):
    return a - b


def mnozenie(a, b):
    return a * b


def dzielenie(a, b):
    return a/b


i = 1;
for row in range(0,3):
    for col in range(0,3):
        button = Button(root, text= i, padx="5", pady="5").grid(row= row, column= col, command=self.buttonClick)
        i+=1

def buttonClick(self):

root.mainloop()
