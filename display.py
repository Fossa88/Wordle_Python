"""
Module designed for printing things to the terminal
"""
from colorama import Fore, Style


def ascii_art():
    """
    print ascii art of the word WORDLE

    :postcondition: print ascii art of the word WORDLE to the terminal
    """
    print(
        "\n\n .----------------.  .----------------.  .----------------.  .----------------.  .----------------. "
        " .----------------.\n"
        "| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. ||"
        " .--------------. |\n"
        "| | _____  _____ | || |     ____     | || |  _______     | || |  ________    | || |   _____      | ||"
        " |  _________   | |\n"
        "| ||_   _||_   _|| || |   .'    `.   | || | |_   __ \    | || | |_   ___ `.  | || |  |_   _|     | ||"
        " | |_   ___  |  | |\n"
        "| |  | | /\ | |  | || |  /  .--.  \  | || |   | |__) |   | || |   | |   `. \ | || |    | |       | ||"
        " |   | |_  \_|  | |\n"
        "| |  | |/  \| |  | || |  | |    | |  | || |   |  __ /    | || |   | |    | | | || |    | |   _   | ||"
        " |   |  _|  _   | |\n"
        "| |  |   /\   |  | || |  \  `--'  /  | || |  _| |  \ \_  | || |  _| |___.' / | || |   _| |__/ |  | ||"
        " |  _| |___/ |  | |\n"
        "| |  |__/  \__|  | || |   `.____.'   | || | |____| |___| | || | |________.'  | || |  |________|  | ||"
        " | |_________|  | |\n"
        "| |              | || |              | || |              | || |              | || |              | ||"
        " |              | |\n"
        "| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' ||"
        " '--------------' |\n"
        "'----------------'  '----------------'  '----------------'  '----------------'  '----------------'"
        "  '----------------' \n")


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


def draw_game(chosen_words, compared):
    """
    Print wordle game to the console

    :param compared: a tuple
    :param chosen_words: a homogeneous dictionary of strings
    :precondition: compared has 5 integers between 0 and 2 inclusive
    :precondition: chosen_words only contains values as 5 letter strings
    :postcondition: wordle game is printed to the console
    :postcondition: chosen_words remains unchanged
    """
    ascii_art()
    for key in range(1, 6):
        for number in range(5):
            if compared[key][number] == 1:
                colour = Fore.YELLOW
            elif compared[key][number] == 2:
                colour = Fore.GREEN
            else:
                colour = Fore.WHITE
            print(colour + '┏━━━┓', end='')
            print(Style.RESET_ALL, end='')
        print()
        for value in range(5):
            if compared[key][value] == 1:
                colour = Fore.YELLOW
            elif compared[key][value] == 2:
                colour = Fore.GREEN
            else:
                colour = Fore.WHITE
            print(colour + f'┃ {chosen_words[key][value]} ┃', end='')
            print(Style.RESET_ALL, end='')
        print()
        for number in range(5):
            if compared[key][number] == 1:
                colour = Fore.YELLOW
            elif compared[key][number] == 2:
                colour = Fore.GREEN
            else:
                colour = Fore.WHITE
            print(colour + '┗━━━┛', end='')
            print(Style.RESET_ALL, end='')
        print()
