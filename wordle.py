"""
Main File for running the game

This shit is going to be so much harder than the new york times version because there is
0 filter on what word gets chosen so have fun with words like gonzo lmao
"""
import random

def intro():
    """
    Display intro to the game in the console

    :postcondition: Prints the intro to the game to the console
    """
    while True:
        print('-----Welcome to wordle in Python-----\n'
              'To start the game input "start"\n'
              'To read the rules of wordle input "rules"')
        user_value = str(input())
        if user_value.lower() == 'start':
            return True
        elif user_value.lower() == 'rules':
            print('\n---How to Play Wordle--- (Copied from nytimes.com)\n'
                  '>> Each guess must be a valid five-letter word.\n\n'
                  '>> The color of a tile will change to show you\n'
                  '   how close your guess was.\n\n'
                  '>> If the tile turns green, the letter is in the\n'
                  '   word, and it is in the correct spot.\n\n'
                  '>> If the tile turns yellow, the letter is in the\n'
                  '   word, but it is not in the correct spot.\n\n'
                  '>> If the tile turns gray, the letter is not in the word.\n')
            input('Press enter to continue when ready!')
        else:
            print('Please enter a valid command\n')


def draw_game(word):
    """
    Print wordle game to the console

    :param word: a string with 5 characters
    :precondition: word is a 5 character string
    :postcondition: wordle game is printed to the console
    """
    pass


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
    intro()
    word = select_word()


if __name__ == '__main__':
    game()
