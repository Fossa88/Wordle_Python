"""
Main File for running the game

This shit is going to be so much harder than the new york times version because there is
0 filter on what word gets chosen so have fun with words like gonzo lmao
"""
import random
import display


def validate_word(inputted_word: str, list_of_words: list):
    """
    Check users word if it is a valid word to use

    :param inputted_word: a string
    :param list_of_words: a homogeneous list of strings
    :precondition: word has only 5 character
    :precondition: list_of_words only contains 5 letter strings
    :postcondition: returns False if word is not 5 characters or inside list_of_words
    :postcondition: returns True if word is 5 characters and inside list_of_words
    :return: a bool True or False

    >>> validate_word('hello', ['hello', 'pizza', 'bigot'])
    True

    >>> validate_word('hell', ['hello', 'pizza', 'bigot'])
    <BLANKLINE>
    hell is not a 5-letter word!
    <BLANKLINE>
    False

    >>> validate_word('hopes', ['hello', 'pizza', 'bigot'])
    <BLANKLINE>
    hopes is not a valid word!
    <BLANKLINE>
    False
    """
    if inputted_word.lower() in list_of_words and len(inputted_word) == 5:
        return True
    elif len(inputted_word) != 5:
        print(f'\n{inputted_word} is not a 5-letter word!\n')
        return False
    else:
        print(f'\n{inputted_word} is not a valid word!\n')
        return False


def select_word():
    """
    Chose random word from words.txt

    :precondition: words.txt has strings inside
    :precondition: words.txt only has 5-letter words
    :postcondition: list_of_words has every 5-letter word in the
                    english language
    :return: list_of_words as a list with every 5-letter word
             in the english language
    """
    list_of_words = []
    with open('words.txt') as file_object:
        for line in file_object:
            cut_word = line[0:5]
            list_of_words.append(cut_word)
    return list_of_words


def confirm_word(inputted_word: str, selected_word: str) -> tuple[int, int, int, int, int]:
    """
    Check how many letters of the user selected work match the selected word

    :param inputted_word: a string
    :param selected_word: a string
    :precondition: inputted_word and selected_word are both have
                    only 5 characters
    :postcondition: inputted_word and selected_word are compared for similarities of characters
    :postcondition: a 2 is appended to a list if a character in inputted_word is the same
                    and in the same spot in as selected_word
    :postcondition: a 1 is appended to a list if a character in inputted_word is the same
                    and is not the same spot in as selected_word
    :postcondition: a 0 is appended to a list if a character in inputted_word is not inside
                    selected_word
    :return: A tuple of integers

    >>> confirm_word('hello', 'hello')
    (2, 2, 2, 2, 2)

    >>> confirm_word('pizza', 'hello')
    (0, 0, 0, 0, 0)

    >>> confirm_word('porch', 'hello')
    (0, 1, 0, 0, 1)
    """
    bool_list = []
    counter = 0
    for letter in inputted_word:
        if letter in selected_word:
            if letter == selected_word[counter]:
                bool_list.append(2)
                counter += 1
            else:
                bool_list.append(1)
                counter += 1
        else:
            bool_list.append(0)
            counter += 1
    return tuple(bool_list)


def check_for_win(compared: dict) -> bool:
    """
    Compared a dictionaries value with a tuple to determine if the word was guessed

    :param compared: A dictionary
    :precondition: compared is a dictionary with values as tuples
    :postcondition: check is True or False based on compared values
    :return: A bool True or False

    >>> check_for_win({1: (2, 2, 2, 2 ,2), 2: (1, 0, 0, 2, 1)})
    False

    >>> check_for_win({1: (1, 2, 2, 2, 2), 2: (1, 1, 1, 1, 1)})
    True
    """
    check = True
    for item in compared.values():
        if item == (2, 2, 2, 2, 2):
            check = False
    return check


def game():
    """
    Drive the game
    """
    play = display.intro()
    list_of_words = select_word()
    word = random.choice(list_of_words)
    print(word)
    compared = {1: (0, 0, 0, 0, 0), 2: (0, 0, 0, 0, 0), 3: (0, 0, 0, 0, 0),
                4: (0, 0, 0, 0, 0), 5: (0, 0, 0, 0, 0), 6: (0, 0, 0, 0, 0)}
    chosen_words = {1: '     ', 2: '     ', 3: '     ', 4: '     ', 5: '     ', 6: '     '}
    counter = 1
    display.draw_game(chosen_words, compared)
    while play:
        user_input = input('Input a 5 letter word: ')
        validation = validate_word(user_input, list_of_words)
        if validation:
            compared[counter] = confirm_word(user_input, word)
            chosen_words[counter] = user_input
            counter += 1
            display.draw_game(chosen_words, compared)
            play = check_for_win(compared)
            if counter == 7 and play != False:
                play = False
                print('\n---Game Over, You Lose!---\n'
                      f'You did not guess the word in 6 tries. The word was {word}!')
            elif counter != 7 and play == False:
                counter -= 1
                print('\n---Game Over, You Win!---\n'
                      f'You successfully guessed the word in {counter}/6 tries!')


if __name__ == '__main__':
    game()
