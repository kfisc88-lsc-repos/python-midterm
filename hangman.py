from random import randint


#----------------------------------------------------------#
# Checks to see if a guess is in the mystery word          #
#----------------------------------------------------------#
def letterCheck(guess, word):
    if guess in word:
        return True
    else:
        return False


#----------------------------------------------------------#
# Returns a random word list from a given list             #
#----------------------------------------------------------#
def randWord(wordList):
    word = wordList[randint(0, len(wordList)-1)]
    return list(word)


#----------------------------------------------------------#
# Displays the currently correctly guessed letters         #
#----------------------------------------------------------#
def currentLetters(guessList, hangmanWord):
    returnList = []
    for guess in hangmanWord:
        if guess in guessList:
            returnList.append(guess)
        else:
            returnList.append("_")
    return returnList





def main():
    #----------------------------------------------------------#
    # Contains the game messages                               #
    #----------------------------------------------------------#
    gameMessages = {"title": "Generic Hangman Game",
                    "description": "Welcome!\nThe object of hangman is to try \
    to guess the letters of a word knowing only the length of \
    the word. Each correct letter guess reveals all instances \
    of the word while three incorrect guesses means you lose.",
                    "incorrect": "Ooooooo, that's the wrong letter. Looks like \
    Mr. Hangman gets another appendage.",
                    "sameGuess": "You've already guessed that. Try again.",
                    "win": "Congratulations! You won!",
                    "lose": "YOU HAVE DIED. Sorry. Lost. Wrong game.",
                    "invalid": "Invalid input, try again.\n"}


    wordList = ["prestidigitation", "coriander", "descriptive", "concentrate",
                 "responsible", "scandalous", "irate", "kindhearted",
                 "adventurous", "permissible", "fascinated", "salami",
                 "warranty", "holiday", "television", "automobile", "xylophone",
                 "excommunicated", "kombucha", "gasoline"]

    run = True # game state

    print(gameMessages["title"])
    print(gameMessages["description"])

    while run:

        #----------------------------------------------------------#
        # Variable initialization/reset                            #
        #----------------------------------------------------------#
        win = False         # bool for win condition
        wrongGuess = 0      # counter for the guessing 'while loop'
        guess = ""          # for holding user guess
        guessList = []      # creates the guessList for storing player guesses
        displayWord = []    # list for holding revealed letters

        # choose a random word and creates a list from it
        hangmanWord = randWord(wordList)

        # Ask player if they want to play or quit
        command = str(input("Would you like to play? [y or n]: "))

        if command.lower() == "y":

            # win/loss conditions
            while (wrongGuess != 3) and (win == False):

                # receive user input for guess
                guess = str(input("\nGuess a letter: \n"))

                # check if guess has already been guessed
                if guess not in guessList:
                    guessList.append(guess)

                    # if guess is in hangmandWord, print revealed letters
                    if letterCheck(guess, hangmanWord):
                        displayWord = currentLetters(guessList, hangmanWord)
                        for character in displayWord:
                            print(character, end = " ")

                        # compare revealed letters to hangmanWord, true = win
                        if displayWord == hangmanWord:
                            win = True

                    # guess not in hangmanWord, increment wrongGuess
                    else:
                        print(gameMessages["incorrect"])
                        wrongGuess += 1

                else:
                    print(gameMessages["sameGuess"])
                    print(guessList, end = " ")

            # checks win/loss status
            if win == True:
                print(gameMessages["win"])
            else:
                print(gameMessages["lose"])

        # ends game instance
        elif command.lower() == "n":
            run = False

        # invalid input catch-all(ish)
        else:
            print(gameMessages["invalid"])
