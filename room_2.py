# Imports
import os
import utils

# Connectecting rooms
import room_1

##############
# Introduction
##############
def introduction(go_back):
    os.system('clear')
    room_2_intro = """            
        <Room 2>\n\n
        <what do they see>\n\n
        <what are their options?.>\n\n
        """     
    print(utils.padToCenter(room_2_intro))
    options(go_back)

#########
# Options
#########
def options(go_back):
    room_2_options_list = [
        'a) option 1', 
        'b) option 2', 
        'c) Go Back'
        ]
    # Arranging items in a list on seperate lines
    for i in room_2_options_list:
        print(i, sep=' ')

    while True:
        option = input("  >> ")
        if option.strip().lower() == 'a':
            print('\n<option 1>\n')
        elif option.strip().lower() == 'b':
            print('\n<option 2>\n')
        elif option.strip().lower() == 'c':
            #beginning_options_minus_intro()     # <--
            go_back(introduction)
            break
        elif option.strip().capitalize() == 'Exit':     # Remove when found a way to make it global
            utils.quitGame()
            break
        elif option.strip().capitalize() == 'None':
            print('\n<sass>\n')
        else:
            print('Type in the letter you choose.\n')
