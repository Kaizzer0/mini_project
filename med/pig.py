import random
def roll():
    min_roll = 1
    max_roll = 6
    roll_score = random.randint(min_roll,max_roll)
    return roll_score

while True:
    num_player = input("How many player you want to play( 2 - 4 ) ? ")
    if num_player.isdigit():
        num_player = int(num_player)
        if 2 <= num_player <=4 :
            break
        else:
            print("Number of player must betwween 2-4")
    else:
        print("Invalid number, please try again!")
        
player_score = [0 for i in range(num_player)]
max_score = 50

while max(player_score) < max_score:
    for player_index in range(num_player):
        current_score = 0
        print("\nThe player" ,player_index + 1, "started to roll !")
        print("your current score is",player_score[player_index])
        current_score = 0

        while True:
            info = input("Do you want to roll the dice ? (y) : ").lower()
            if info != "y":
                break

            score = roll()
            print("you have roll a ", score)
            if score == 1:
                current_score = 0
                print("Oh no ! u roll a 1 so your current score will turn to 0 :(((")
                break
            else :
                current_score += score 
                print("your current score is ",current_score)

        player_score[player_index] += current_score
        print("your total score is :", player_score[player_index])

max_score = max(player_score)
win_index = player_score.index(max_score)

print("player number" ,win_index + 1, "is win")
print("The score is :",max_score)