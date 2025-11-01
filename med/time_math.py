import random 
import time

OPERATOR = ["+", "-", "*"]
min = 1
max = 12
total = 3

def generate_op():
    MIN = random.randint(min,max)
    MAX = random.randint(min,max)
    op = random.choice(OPERATOR)
    exp = str(MIN) + " " + op + " " + str(MAX)
    answer = eval(exp)
    return exp,answer


input("Press enter to start! ")
start_time = time.time()
for i in range(total):
    exp,answer = generate_op()
    while True:
        guess = input("problem #" + str(i+1) + ": " + exp + " = ")
        if guess == str(answer):
            break
        

end_time = time.time()
total_time = round(end_time - start_time,2)
print("You have win the game in " + str(total_time) + " seconds!")