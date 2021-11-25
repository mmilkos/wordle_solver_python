from tkinter import *

root = Tk()
root.title('Kalkulator')

first_num = ""
second_num = ""
isButtonClicked = False


first_holder = []
second_holder = []

e = Entry(root, width=35, borderwidth=5, state='disabled')
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_add(but):
    if not isButtonClicked:
        first_holder.append(str(but['text']))
        first_num = ("".join(first_holder))
        print(first_num)
    else:
        second_holder.append(str)


i = 9
r = 3
c = 3
for row in range(0, r):
    for col in range(0, c):
        button = Button(root, text=i, padx="40", pady="20")
        button.grid(row=row + 2, column=c - col)
        button['command'] = lambda btn = button: button_add(btn)
        i -= 1

buttonPlus = Button(root, text='+', padx="39", pady="19")
buttonPlus.grid(row=row + 3, column=c - col)
buttonPlus['command'] = lambda x = first_num, y = second_num: print(x + y)
buttonMinus = Button(root, text='-', padx="39", pady="19")
buttonMinus.grid(row=row + 3, column=c - col + 1)
buttonMultiply = Button(root, text='*', padx="39", pady="20")
buttonMultiply.grid(row=row + 3, column=c - col + 2)
buttonDivide = Button(root, text='/', padx="39", pady="20")
buttonDivide.grid(row=row + 4, column=c - col)

[]


root.mainloop()

