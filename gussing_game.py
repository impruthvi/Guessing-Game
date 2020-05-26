import random

random_number = random.randint(1,10)


while True:
    guess = input("PIC UP A NUMBER FROM 1 TO 10: ")
    guess = int(guess)
   
    if  guess < random_number:
        print("to low")
    elif guess > random_number:
        print("to high")
    else:
        print("you won")
        play_again = input("You wont to Play again?(y/n)")
        if play_again == 'y':
             guess = input("PIC UP A NUMBER FROM 1 TO 10: ")
             guess = None
        else:
            print("Thanks for Playing....")
            break