# Imports
import os
import utils                     # This imports ALL code, right here and now, from the file 'utils.py'. Referencing entries, e.g. functions, variables, requires using the qualifying module name, e.g. 'utils.<function>' or 'utils.<variable>'
# from config import padToCenter    # This imports just the code requested, i.e. 'padToCenter' and allows the function/variable to be referenced without the module name, but, there cannot be a conflict with other functions/variables. Also, not good to import the entire modele then parts of a module...

# Connectecting rooms
import room_2
import room_3

##############
# Introduction
##############
def introduction(go_back):
    os.system('clear')
    intro = """            
        <Story text about waking up in a room>\n\n
        <Describe what the player sees in brief.>\n\n
        What do you do?
        """     
    print(utils.padToCenter(intro))
    options(go_back)

#########
# Options
#########
def options(go_back):
    utils.printOptions([
        'a) Go through the door to your left', 
        'b) Go through the door to your right', 
        'c) Explore',
        'd) Go back'
        ])

    while True:
        option = utils.getOption()
        if  option == 'a':
            room_2.introduction(introduction)     # Pass THIS room's introduction function as the 'go back' room for room_2
            break
        elif option == 'b':
            room_3.introduction(introduction)
        elif option == 'c':
            explore()
            break
        elif option == 'd':
            go_back(introduction)
            break
        elif option == 'exit':
            utils.quitGame()
            break
        elif option == 'none':
            print('\n<sass>\n')
        else:
            print('Type in the letter you choose.\n')

#########
# Explore
#########
def explore():
    utils.printCentered("""            
        \n<Story text about finding a note from self and your wallet>\n
        """     
        )

    utils.printOptions([
        'a) Read note', 
        'b) Go through wallet',
        'c) Back'
        ])

    while True:
        option = utils.getOption("  >> ")

        if option == 'a':
            os.system('clear')  
            print('\n<Note>\n')  # Add Note details         
            input('Return? >> ') 
            explore()   
            break       
        
        if option == 'b':
            os.system('clear')
            utils.check_player_name()
            explore()
            break

        if option == 'c':
            options()
            break
        
        if option == 'exit':      # Remove when found a way to make it global
            utils.quitGame()
            return
        
        if option == 'none':
            print('\n<sass>\n')
            return
        
        print('\nType in the letter you choose.\n')