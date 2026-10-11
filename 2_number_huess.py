import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input("enter your guessed number between 1 and {x}: "))
        if guess < random_number:
            print(f"oops! sorry try again you are TOO low!:")
        elif guess > random_number:
            print(f"oops! sorry try again you are Too high!")

        else:
            print(f"yayy! congrats you have guessed {random_number} correctly!")    



guess(3)



