import random
user_score = 0
comp_score = 0
option = ['rock','paper','scissor']
while True:
    ran_num = random.randint(0,2)
    user_input = input("Type the rock/paper/scissor or type q to quit the game: ").lower()
    if user_input == "q":
        break

    if user_input not in option:
        continue

    com_input = option[ran_num]
    print("computer pick",com_input + '.')

    if user_input == 'rock' and com_input == 'scissor':
        print('YOU WIN')
        user_score += 1
    
    elif user_input == 'paper' and com_input == 'rock':
        print('YOU WIN')
        user_score += 1

    elif user_input == 'scissor' and com_input == 'paper':
        print('YOU WIN')
        user_score += 1

    else:
        print('TRY AGAIN NEXT TIME ')
        comp_score += 1

print('computer have win:', comp_score , 'time')
print('you have win:', user_score , 'time')
