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
	# 1. if they guess a letter loop over the  list and see if its in their, if it is make it appear in its location ,except for the letter that the user guessed they appear as _:
def hiden_words(guessed,words):

	guessed_letter= []
	# loop through the parameter words(possible_words) and then loop through each of its letters
	for word in words:
		for letter in words:
			print(letter)
			if guessed == letter:
				#if what the user gussed is in letter then add it to guessed_letter
					guessed_letter += letter
			# if its not show it as _ instead
			else:
				guessed_letter += "_"
		return guessed_letter

possible_words = ['ungulate', 'lungfish', 'axolotl', 'blobfish']
print("Let's play Hangman!\n")
while True:
	print("Enter a letter")
	guess = input('> ')
	print(hiden_words(guess,possible_words))
	if guess == 'quit':
		break
