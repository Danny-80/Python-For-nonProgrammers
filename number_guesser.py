import random
import time

print('Hi! Welcome to the guessing name. Please guess a number between 1 and 100.')
time.sleep(1)
print('Picking a number...')
time.sleep(2)
guess = int(input("What is your guess? "))
correct_num = random.randint(1,100)
guess_count = 1

while guess != correct_num:
    guess_count += 1
    if guess < correct_num:
        guess = int(input("Wrong. You need to guess higher number. What is your guess? "))
    elif guess > correct_num:
        guess = int(input("Wrong. You need to guess lower number. What is your guess? "))
     
print(f'Congrats! The right answer was {correct_num}. It took you {guess_count} guesses.')
