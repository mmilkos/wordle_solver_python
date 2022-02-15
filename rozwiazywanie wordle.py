from classes import Create, Remove, all_words


def start_solving():
    Create.create_array()
    print(f'recommended first words: crane, tried, slice')

    while True:
        if len(all_words) == 1:
            break

        user_input = input(f'Enter a word or press X to exit : ').lower()
        if user_input.strip() == 'x':
            break
        if Create.check_word_len(user_input):
            Remove.delete_word(user_input)
            print(f'Suggested word: {Create.possible_words()}')
        else:
            continue


start_solving()
