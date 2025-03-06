#printing FizzBuzz if number is divisible by 3 and 5, print Fizz if divisible by 3, and printing Buzz if divisible by 5

def fizzBuzz(upTo):
	for number in range(1,upTo):
		if number % 3 == 0 and number % 5 == 0:
			print('FizzBuzz', end=" ")
		elif number % 3 == 0:
			print('Fizz', end=" ")
		elif number % 5 == 0:
			print('Buzz', end=" ")
		else:
			print(number, end=" ")
fizzBuzz(35)