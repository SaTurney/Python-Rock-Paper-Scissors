#Sabrina Turney
#November 26, 2018
#Rock, Paper, Scissors
#This is a Rock, Paper, Scissors game. The typical rules of Rock, Paper,
#Scissors apply, except in this case, there are required modules, as well
#as required menus, consisting of "Main Menu" and "Weapon Menu".
#Two players are able to play this game, or a player can play against a computer,
#but the game should display scores for both players and continue until
#someone chooses the option to quit the game.


#Because our 1-player game mode needs computer input, we import the random
#module, that way the player can win or lose against the computer.
from random import randint


#My introduction below. Throws the info at the user quickly, so they'll
#understand the functionality of the program without a
#big paragraph. They want to get into the game!
def intro():
    print("Welcome to my Rock, Paper, Scissors game!")
    print("In this program, you can play forever, if you want!")
    print("And if you don't have a friend to play with, I'll play with you!")

def menu(menuInput):
    print('\n\n----------Main Menu----------')
    print('''1.See the Rules
2.Play against the computer
3.Play a two player game
4.Quit''')
#I used a triple quote here to make the display easier for the user to digest.

    #Input validation begins here, as does us calling each module depending
    #on the user input.
    menuInput = int(input('\n\tPlease enter a number 1 - 4 to continue: '))
    while menuInput <1 or menuInput >4:
        print('Please enter a value of 1 - 4 to continue: ')
        menuInput = int(input('\n\tPlease enter a number 1 - 4 to continue: '))
    return menuInput

#Here's the meat of the program, where we let the user decide to keep
#playing, or quit. We call all our main menu module within it. The specific
#Main Menu is not used here, but will run every time the program begins,
#or when the user enters the correct number. We also declare our boatload
#of variables!
def main():
    endProgram = "no"
    playMore = "yes"
    menuInput = 0
    onePlayer = 0
    comChoice = 0
    oneChoice = 0
    twoChoice = 0
    scoreOne = 0
    scoreTwo = 0

    #I call the intro module before the loop begins to avoid an intro every time
    #a user asks to return to the main menu.
    intro()

    #Here the program begins to run in a loop. You choose from the menu or else!
    #Depending on the user input for the menu, we call different functions, or
    #quit the program and say goodbye.
    while endProgram == "no":
        menuInput = menu(menuInput)
        print('\n\nYou\'ve chosen option: ', menuInput)
        print('\n\n')
        if menuInput == 1:
            print('''The rules are as follows:
1.Paper covers Rock
2.Rock smashes Scissors
3.Scissors cuts Paper''')
        #For playing against the computer vs player, I reuse variables, because
        #once a game is quit, the main menu is re-ran (so scoreOne/scoreTwo)
        #are interchangeable, as well as "playMore".
        elif menuInput == 2:
            onePlayer, comChoice, playMore, scoreOne, scoreTwo = computer(onePlayer, comChoice, playMore, scoreOne, scoreTwo)
        elif menuInput == 3:
            oneChoice, twoChoice, playMore, scoreOne, scoreTwo = twoplayer(oneChoice, twoChoice, playMore, scoreOne, scoreTwo)

        #Here's the easy way out- Our quit program for number 4.
        elif menuInput == 4:
            print('Do you want to quit the program now?')
            endProgram = input('Enter "yes" now to exit! ')
            while endProgram == 'yes' or endProgram != 'no':
                print('\nThanks for playing! Goodbye!')
                return

#Here's our computer vs user module! We let the player know it's a computer,
#then implement the weapons menu to get our choices chosen.
def computer(onePlayer, comChoice, playMore, scoreOne, scoreTwo):
    print('Great! You\'re facing the computer.')
    print('Choose your weapon from the weapons menu:')
    print('\n\n----------Weapons Menu----------')
    print('''1.Rock
2.Paper
3.Scissors
4.Return to Main Menu''')

    #The playMore variable allows us to have multiple rounds in a while loop.
    playMore = "yes" 

    while playMore == "yes":
        #More input validation, must be in the menu.
        onePlayer = int(input("\n\tPlease enter a number 1 - 4 to continue: "))
        while onePlayer<0 or onePlayer>4:
            print('Please enter a number 1 - 4 to continue: ')
            onePlayer = int(input("\n\tPlease enter a number 1 - 4 to continue: "))

        #Here we use the random built-in library to have the computer choose
        #its weapon. We only use 1-3 because the computer shouldn't be able
        #to rage quit a game.
        comChoice = randint(1,3)
        #I chose to have the computer's choice print out so the user knows
        #how they won or lost visually instead of having to think for a second.
        print('\tThe computer chose: ', comChoice)

        if onePlayer == 4:
            print('\nTaking you back to the main menu!\n')
            main()
            #If user enters 4, we take them back to the main menu.

        #This If/Elif block finds all possible combinations of rock, paper, and
        #scissor, then adds points depending on who won each round. Ties award 0
        if comChoice == onePlayer:
            print('\nIt\'s a tie!')
        elif comChoice == 1 and onePlayer == 2:
            print('You win! Congratulations!')
            scoreOne += 1
        elif comChoice == 1 and onePlayer == 3:
            print('The computer wins this round!')
            scoreTwo += 1
        elif comChoice == 2 and onePlayer == 1:
            print('The computer wins this round!')
            scoreTwo += 1
        elif comChoice == 2 and onePlayer == 3:
            print('You win! Congratulations!')
            scoreOne += 1
        elif comChoice == 3 and onePlayer == 1:
            print('You win! Congratulations!')
            scoreOne += 1
        elif comChoice == 3 and onePlayer == 2:
            print('The computer wins this round!')
            scoreTwo += 1

        #After each round of play, the score of each player is posted.
        print('The current score is: Player 1, ', scoreOne)
        print('The computer\'s score is: ', scoreTwo)

        #Here's the point where a user decides to play another round and
        #continue adding scores, or quit and return to the main menu.
        playMore = input('Would you like to play again? ')
        if playMore != "no":
            computer(comChoice, onePlayer, playMore, scoreOne, scoreTwo)
            return comChoice, onePlayer, playMore, scoreOne, scoreTwo



    return onePlayer, comChoice, playMore, scoreOne, scoreTwo


#This is our two player game module! We use some similar variables we need,
#like playing again, keeping scores, and choices. 
def twoplayer(oneChoice, twoChoice, playMore, scoreOne, scoreTwo):
    #We let the player know they've chosen the two player game option and
    #present the essential weapons menu.
    print('Great! You\'re facing a friend.')
    print('Choose your weapons from the weapons menu:')
    print('\n\n----------Weapons Menu----------')
    print('''1.Rock
2.Paper
3.Scissors
4.Return to Main Menu''')
    playMore = "yes"

    #Our while loop begins again to start the play by rounds, just like in the
    #computer module, except either user can choose to quit.
    while playMore == "yes":
        oneChoice = int(input('\n\tPlayer 1, please choose your weapon now: '))
        while oneChoice<0 or oneChoice>4:
                print('Please enter a number 1-4 to continue!')
                oneChoice = int(input('\n\tPlayer 1, please choose your weapon now: '))

        twoChoice = int(input('\n\tPlayer 2, please choose your weapon now: '))
        while twoChoice<0 or twoChoice>4:
                print('Please enter a number 1-4 to continue!')
                twoChoice = int(input('\n\tPlayer 2, please choose your weapon now: '))
        
        if oneChoice == 4 or twoChoice == 4:
            print('\nTaking you back to the main menu!\n')
            main()
        #Again, I get all possible combinations of rock, paper, scissors for
        #both players, and then add scores for each win.
        if oneChoice == twoChoice:
            print('\nIt\'s a tie!')
        elif oneChoice == 1 and twoChoice == 2:
            print('\nPlayer 2, you win! Congratulations!')
            scoreTwo += 1
        elif oneChoice == 1 and twoChoice == 3:
            print('\nPlayer 1, you win! Congratulations!')
            scoreOne += 1
        elif oneChoice == 2 and twoChoice == 1:
            print('\nPlayer 1, you win! Congratulations!')
            scoreOne += 1
        elif oneChoice == 2 and twoChoice == 3:
            print('\nPlayer 2, you win! Congratulations!')
            scoreTwo += 1
        elif oneChoice == 3 and twoChoice == 2:
            print('\nPlayer 1, you win! Congratulations!')
            scoreOne += 1
        elif oneChoice == 3 and twoChoice == 1:
            print('\nPlayer 2, you win! Congratulations!')
            scoreTwo += 1

        #Just like with the computer module, after every round, a score
        #is displayed.
        print('The current score is: Player 1, ', scoreOne)
        print('Player 2, your score is: ', scoreTwo)

        #If the game is quit, we return to the main menu, or we continue
        #adding scores and starting rounds over.
        playMore = input('Would you like to play again? ')
        if playMore != "no":
            twoplayer(oneChoice, twoChoice, playMore, scoreOne, scoreTwo)
            return oneChoice, twoChoice, playMore, scoreOne, scoreTwo

#Lastly, we call the main function for the user.      
main()
