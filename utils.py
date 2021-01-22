import os 
import sys

# Global variables
player_name = ''

##############
# Utility functions
##############
def printCentered(text:str):
    print(padToCenter(text))

# Centering multi-line text
def padToCenter(text)->str:         # This code adapted from stuff I found on Stack Overflow. I don't fully understand it yet.
    """Manual centering"""
    l = text.splitlines()
    width = os.get_terminal_size().columns      # Figures out how to center objects based on current window size
    padding =  ' '*(width//2)           # a 1 char line would need at most w/2 spaces in front
    parts = [ padding[0: (width-len(p))//2+1]+p for p in l]
    return '\n'.join(parts)

def getOption(prompt="  >> "):
    return input(prompt).strip().lower()

def printOptions(options_list:list):
    for i in options_list:
        print(i, sep=' ')

# Quit the game
def quitGame():
    print('Goodbye!')
    sys.exit()

##########
# Player name functions
##########
def get_player_name()->str:
    return player_name  # Return the global player_name, defined above (at the top of this file)

##########
def set_player_name(incoming_player_name:str):
    global player_name
    player_name = incoming_player_name

##########
def check_player_name():
    if get_player_name() == '':
        print('''\n<details of wallet contents> You look closely at the ID card.  Below the name section you read...\n\n What is your name?\n''')    
        player_name = input('  >> ')
        while player_name == '':
            print("\nSurely there must be something written there.  Take another look.\n")
            player_name = input('  >> ')
        print('\nHmm, '+player_name.capitalize().strip()+'.  Yes, that sounds right.\n')
        set_player_name(player_name)
        input('Return? >> ')
    else:
        print("\nYou have already discovered that your name is "+get_player_name().capitalize().strip()+". Would you like to double check?\n")
        while True:
            pos_responses = ['yi', 'yes', 'y', 'yep']
            neg_responses = ['nah', 'no', 'n', 'nope']
            double_check = input(" Yes/No?  >> ")
            if double_check.lower().strip() in pos_responses:
                break
            elif double_check.lower().strip() in neg_responses:
                print('\nOk, '+get_player_name().capitalize().strip()+' it is!\n')
                return
            else:
                print("Type yes or no.")
        
        print('\nYou double check your name.\n\n What is your name?\n')
        while True:
            player_name = input('  >> ')
            if player_name =='':
                print("\nSurely there must be something written there.  Take another look.\n")
            else:
                set_player_name(player_name)
                break
        print('\nAfter removing a large smudge of dirt you discover your name is actually '+get_player_name().capitalize().strip()+'.  Yes, that sounds better.\n')     
        input('Return? >> ')


