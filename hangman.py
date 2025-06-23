# Create a hangman game!

# The game should:
# - Pick a random word.
# - Before each guess, display these two things:
#     1. the current word, using underscores for letters that haven't been correctly guessed yet, like this: "_ _ a _" (the third letter is "a")
#     2. the list of incorrect guesses (in the order they were given), like this: "Guessed: a w b"
# - On the seventh incorrect guess, the player loses the game (display a message and break out of the loop).
# - On revealing the entire word, the player wins the game (display a message and break out of the loop).
# - You should validate that the input is valid: must be one letter, a to z. Be sure to handle capital letters, but I'll leave how up to you. If the input is invalid, tell the player.

# I encourage you to make methods for each piece of logic! You could imagine methods for things like displaying the word before each guess, knowing if the user has won, or knowing if the guess is correct.

# 1. creat a function that stores gussed letter if they are the same as  letters in possible_words
# 1. if they guess a letter loop over the  list and see if its in their, if it is make it appear in its location ,except for the letter that the user didnt guessed they appear as _:
# endgame:   # TODO make a method that registers guess into the right variable,make a methode that shows True if wone False if lost

#  anyhting i need to track make a variable, pick a word from the list, what global variables do you think you need?
def display_word(word,guessed_letters):
    #store the guessed letters
    correct_letters = ""
	# loop through the parameter words(possible_words) and then loop through each of its letters
    print("guessedletters:",guessed_letters)
    for letter in word:
        if letter in guessed_letters:#checks if the guessed letters are in possible word
            correct_letters += letter

			# if its not show it as _ instead
        else:
            correct_letters += " _ "
    return correct_letters

def play_game():
    print("i am in play games")

    incorrect_letters = []#stores incorrect guesses
    guessed_letters = ''
    # TODO make a list of words and possible_word will pick from it
    word = 'ungulate'
    print("Let's play Hangman!\n")
    while True:
        print("Enter a letter")
        guess = input('> ')
        # TODO: dont put the same letter in incorrect_letter twice
        if guess not in guessed_letters:
            guessed_letters += guess #everytime it loops it adds the inputs to guess
        if guess not in word:#2. make a variable for all of the incorrect guess and display it
            incorrect_letters += guess
            print("incorrect letters:",incorrect_letters)
            # 2.1 # - On the seventh incorrect guess, the player loses the game (display a message and break out of the loop).
            if len(incorrect_letters) >= 7: # stops the loop when it reaches 7 wrong letters
                    print("to many wrong answeres you lose :(")
                    break
            #2.2 On revealing the entire word, the player wins the game (display a message and break out of the loop).
        current_progress = display_word(word,guessed_letters) # shows the current displayed letters
        print("progress",current_progress)# shows how many left untill all _ is replaced
        if "_" not in current_progress:# checks if theirs isnt anymore _ left
            print("congratulation you win")
            break
        if guess == 'quit':
            break
        # start:2-3 You should validate that the input is valid: must be one letter, a to z. Be sure to handle capital letters, but I'll leave how up to you. If the input is invalid, tell the player.

        # q:how do i make it so the code check for duplicat letter?
        #store all the guessed letters in a list
        #use count to check for dupes in that list
        if guess in guessed_letters:#checks if the letter is already guessed
            print("you already guessed that letter, try again")

        # print("all guessed letters:",all_guessed_letters)
        #end: if the user trys to input the same letter raise an error
play_game()
