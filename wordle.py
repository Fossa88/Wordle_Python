"""
Main File for running the game

This shit is going to be so much harder than the new york times version because there is
0 filter on what word gets chosen so have fun with words like gonzo lmao
"""
import random
import display

def select_word():
    """
    Chose random word from words.txt

    :precondition: words.txt has strings inside
    :precondition: words.txt only has 5-letter words
    :postcondition: word is a random 5-letter word from
                    the english language
    :return: word as a string of a 5-letter word
    """
    list_of_words = []
    with open('words.txt') as file_object:
        for line in file_object:
            list_of_words.append(line)
    word = random.choice(list_of_words)
    return word


def game():
    """
    Drive the game
    """
    play = display.intro()
    word = select_word()
    chosen_words = {1: '     ', 2: '     ', 3: '     ', 4: '     ', 5: '     '}
    counter = 1
    while play:
        display.draw_game(word, chosen_words)
        user_input = input('Input a 5 letter word')
        chosen_words[counter] = user_input
        counter += 1


if __name__ == '__main__':
    game()
