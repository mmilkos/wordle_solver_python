import re
import random

all_words = []


class Logic:
    def __init__(self):
        pass

    @staticmethod
    def creating_array():
        with open('slowa.txt') as words:
            for word in words:
                all_words.append(word.rstrip('\n'))

    @staticmethod
    def check_word_len(word):
        if len(word) == 5:
            return True
        else:
            return False

    @staticmethod
    def deleting_words(word):
        global all_words
        grey_letters = input('Which letters are gray?: ').strip()

        for letter in grey_letters:
            all_words = [element for element in all_words if element.count(letter) == 0]

        green_letters = input('Which letters are green?: ').strip()
        for letter in green_letters:
            all_words = [element for element in all_words if element.find(letter) == word.find(letter)]

        yellow_letters = input('Which letters are yellow?: ').strip()
        for letter in yellow_letters:
            all_words = [element for element in all_words
                         if letter in element and element.find(letter) != word.find(letter)]


def start_solving():
    Logic.creating_array()
    while True:
        if len(all_words) == 1:
            print(all_words[0])
            break
        user_input = input(f'Enter a word or press X to exit : ').lower()
        if user_input.strip() == 'x':
            break
        if Logic.check_word_len(user_input):
            Logic.deleting_words(user_input)
            print(all_words)
            print(f'Suggested word: {all_words[random.randint(0, len(all_words) - 1)]}')
        else:
            continue


start_solving()
