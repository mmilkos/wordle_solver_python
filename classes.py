import random

all_words = []


class Create:
    def __init__(self):
        pass

    @staticmethod
    def create_array():
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
    def possible_words():
        choices = ''

        if len(all_words) < 11:
            for word in all_words:
                choices = choices + word + ' '
            return choices
        else:
            for i in range(3):
                choices = choices + str(random.choice(all_words)) + ' '
            return choices


class Remove:
    def __init__(self):
        pass

    @staticmethod
    def delete_word(word):
        global all_words
        all_letters = []

        if len(all_letters) < 6:
            grey_letters = input('Which letters are gray?(skip if letter is both green and grey): ').strip()
            for letter in grey_letters:
                all_words = [element for element in all_words if element.count(letter) == 0]
                all_letters.append(letter)

        if len(all_letters) < 5:
            green_letters = input('Which letters are green?: ').strip()
            for letter in green_letters:
                all_words = [element for element in all_words if element.find(letter) == word.find(letter)]
                all_letters.append(letter)

        if len(all_letters) < 5:
            yellow_letters = input("Which letters are yellow?(skip if letter is both green and yellow): ").strip()
            for letter in yellow_letters:
                if letter not in green_letters:
                    all_words = [element for element in all_words if letter in element]
                    all_letters.append(letter)

        print(f'Words left {len(all_words)}')
