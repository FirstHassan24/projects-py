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

possible_words = ['ungulate', 'lungfish', 'axolotl', 'blobfish']
#store the guessed letters:
guessed_letter= []
print("Let's play Hangman!\n")
while True:
	print("Enter a letter")
	guess = input('> ')
	for word in possible_words:
# 1. if they guess a letter loop over the  list and see if its in their, if it is make it appear as _ except for the letter that the user guessed:
		for letter in word:
			# print(letter)
			if guess == letter:
				guessed_letter += guess
				# print(guess)
        # ^this should not print their is no h in letter
			else:
				print("_")
			if guess == 'quit':
				break
