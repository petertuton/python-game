# Opening - First Riddle
import os
import utils

import room_1

def intro(go_back):
    os.system('clear')
    print('Created from 9 Jan 2021 - <insert finished date>\n\nBy J.D. Ridley Tuton\n\n')
    input('Press <Enter>')

    # Entering game
    os.system('clear')
    print('<title of game>\n\n'.center(os.get_terminal_size().columns))
    print("Type 'Anything' to continue OR 'Exit' to quit\n")
    print("Type 'Exit' at any time to quit the game.\n")

    # Will keep you answering until the typed response is 'anything'
    while True:
        x = input("  >> ")
        if x.strip().capitalize() == 'Anything':
            room_1.introduction(intro)
            break
        elif x.strip().capitalize() == 'Exit':
            utils.quitGame()
            break
        else:
            print('\nTry Again!\n')
