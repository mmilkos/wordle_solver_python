from tkinter import *
import random

root = Tk()
root.title('Fiszki')
root.geometry("550x410")

with open('txt.txt') as r:
    words = [tuple(map(str, i.split(','))) for i in r]

words_counter = len(words) - 2

en_words = Label(root, text='')

pl_words = Label(root, text="", font=155)
pl_words.pack(pady=50)

user_input = Entry(root)
user_input.pack(pady=10)

# Create Buttons
b_frame = Frame(root)
b_frame.pack(pady=20)

answer_button = Button(b_frame, text="Answer")
answer_button['command'] = lambda y=answer_button: answer()
answer_button.grid(row=0, column=0, padx=20)

skip_button = Button(b_frame, text="Skip")
skip_button['command'] = lambda x=skip_button: skip()
skip_button.grid(row=0, column=1, )


def skip():
    random_number = random.randint(0, words_counter)
    en_words.config(text=words[random_number][0])
    pl_words.config(text=words[random_number][1])
    user_input.delete(0, 'end')


def answer():
    if user_input.get() == en_words['text']:
        print('poprawnie')
        skip()


skip()

root.mainloop()

# siema no
