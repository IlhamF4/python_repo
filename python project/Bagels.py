import random

NUM_DIGIT = 3
MAX_GUESS = 10

def main():
	print("""Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a {}-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.
	""".format(NUM_DIGIT))
	while True:
		print('I have thought of a number.')
		print('you have {} guesses to get it.'.format(MAX_GUESS))
		secretNum = getSecretNum()
		numGuesses = 1
		while numGuesses <= MAX_GUESS:
			guess = ' '
			while len(guess) != NUM_DIGIT or not guess.isdecimal():
				print('Guess #{}: '.format(numGuesses))
				guess = input('> ')
			
			clues = getClues(guess, secretNum)
			print(clues)
			numGuesses += 1
			
			if guess == secretNum:
				break
			if numGuesses > MAX_GUESS:
				print('You ran out of guesses.')
				print('The answer was {}'.format(secretNum))
		print('Do you want to play again? (yes or no)')
		if not input('>  ').lower().startswith('y'):
			break
	print('Thanks for playing!')

def getSecretNum():
	numbers = list('012345678')
	random.shuffle(numbers)
	secretNum = ''
	for i in range(NUM_DIGIT):
		secretNum += str(numbers[i])
	return secretNum

def getClues(guess, secretNum):
	if guess == secretNum:
		return 'You got it'
	
	clues = []
	
	for i in range(len(guess)):
		if guess[i] == secretNum[i]:
			clues.append('Fermi')
		elif guess[i] in secretNum:
			clues.append('Pico')
	if len(clues) == 0:
		return 'Bagels'
	else:
		clues.sort()
		return " ".join(clues)
	
if __name__ == '__main__':
	main()