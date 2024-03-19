#Generate a secret number under 10 and take a guess. Win with the right number or try again for the ultimate gaming fun.

import random

secret_number = random.randint(1, 10)
guess = int(input("Guess the secret number (between 1 and 10): "))

if guess == secret_number:
    print("Congratulations! You guessed the secret number!")
else:
    print("Sorry, that's not the right number. The secret number was:", secret_number)
