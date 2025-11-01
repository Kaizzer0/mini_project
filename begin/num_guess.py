import random
print("Hello welcome to guess number game")
range_to_guess = input('Type an number to check ')
if range_to_guess.isdigit():
    range_to_guess = int(range_to_guess)
    if range_to_guess < 0:
        print("please type a number greater than 0 next time")
else:
    print("Please type an number !!!")
    quit()

ran = random.randint(0,range_to_guess)
guess = 0
while True:
    guess += 1 
    user_guess = input("Make a guess ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please type an number!")
        continue

    if user_guess == ran:
        print("YOU WIN THE GAME")
        break
    else:
        if user_guess > ran :
            print("Your guess is higher than the number :((")
        elif user_guess < ran:
            print("Your guess is lower than the number :((")
print("Your Total Guess is :",guess)
