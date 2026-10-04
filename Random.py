import random


low = 1
high = 100
guesses = 0
num = random.randint(low, high)
while True:
    guess = int(input(f"Enter your number between {low} to {high} :"))
    guesses += 1
    if guess < num :
        print(f"Your gess {guess} is too low")
    elif guess > num:
        print(f"Your gess {guess} is too high")
    else:
        print(f"! You won ! ")
        break

print(f"Correct answer is {num} and you took {guesses} guesses ")
