"""
Module designed for printing things to the terminal
"""

def intro():
    """
    Display intro to the game in the console

    :postcondition: Prints the intro to the game to the console
    :return: Bool True or False
    """
    while True:
        print('-----Welcome to wordle in Python-----\n'
              'To start the game input "start"\n'
              'To read the rules of wordle input "rules"\n'
              'To quit the module input "quit"')
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
        elif user_value.lower() == 'quit':
            return False
        else:
            print('Please enter a valid command\n')


def draw_game(word, chosen_words):
    """
    Print wordle game to the console

    :param word: a string with 5 characters
    :param chosen_words: a homogeneous dictionary of strings
    :precondition: word is a 5 character string
    :precondition: chosen_words only contains values as 5 letter strings
    :postcondition: wordle game is printed to the console
    :postcondition: chosen_words remains unchanged
    """
    print('┏━━━┓ ┏━━━┓ ┏━━━┓ ┏━━━┓ ┏━━━┓\n'
          f'┃ {chosen_words[1][0]} ┃ ┃ {chosen_words[1][1]} ┃ ┃ {chosen_words[1][2]}'
          f' ┃ ┃ {chosen_words[1][3]} ┃ ┃ {chosen_words[1][4]} ┃\n'
          '┗━━━┛ ┗━━━┛ ┗━━━┛ ┗━━━┛ ┗━━━┛\n'
          '┏━━━┓ ┏━━━┓ ┏━━━┓ ┏━━━┓ ┏━━━┓\n'
          f'┃ {chosen_words[2][0]} ┃ ┃ {chosen_words[2][1]} ┃ ┃ {chosen_words[2][2]}'
          f' ┃ ┃ {chosen_words[2][3]} ┃ ┃ {chosen_words[2][4]} ┃\n'
          '┗━━━┛ ┗━━━┛ ┗━━━┛ ┗━━━┛ ┗━━━┛\n'
          '┏━━━┓ ┏━━━┓ ┏━━━┓ ┏━━━┓ ┏━━━┓\n'
          f'┃ {chosen_words[3][0]} ┃ ┃ {chosen_words[3][1]} ┃ ┃ {chosen_words[3][2]}'
          f' ┃ ┃ {chosen_words[3][3]} ┃ ┃ {chosen_words[3][4]} ┃\n'
          '┗━━━┛ ┗━━━┛ ┗━━━┛ ┗━━━┛ ┗━━━┛\n'
          '┏━━━┓ ┏━━━┓ ┏━━━┓ ┏━━━┓ ┏━━━┓\n'
          f'┃ {chosen_words[4][0]} ┃ ┃ {chosen_words[4][1]} ┃ ┃ {chosen_words[4][2]}'
          f' ┃ ┃ {chosen_words[4][3]} ┃ ┃ {chosen_words[4][4]} ┃\n'
          '┗━━━┛ ┗━━━┛ ┗━━━┛ ┗━━━┛ ┗━━━┛\n'
          '┏━━━┓ ┏━━━┓ ┏━━━┓ ┏━━━┓ ┏━━━┓\n'
          f'┃ {chosen_words[5][0]} ┃ ┃ {chosen_words[5][1]} ┃ ┃ {chosen_words[5][2]}'
          f' ┃ ┃ {chosen_words[5][3]} ┃ ┃ {chosen_words[5][4]} ┃\n'
          '┗━━━┛ ┗━━━┛ ┗━━━┛ ┗━━━┛ ┗━━━┛\n')
