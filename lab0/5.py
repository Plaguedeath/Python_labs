import random
random_number = random.randint(1,100)
guess = None
while guess != random_number:
    guess = int(input("Try to guess a number:"))
    if guess > random_number:
        print("Try lower number")
    elif guess < random_number:
        print("Try higher number")
    else:
        print("You've got it!")
    
