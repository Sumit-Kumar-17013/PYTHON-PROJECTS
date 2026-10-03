import random
import time

OPRATORS = ["+" , "-" , "*" ]
MIN_VALUE = 2
Max_VALUE = 20
total_problem = 10

def problem_generator():
    left = random.randint(MIN_VALUE , Max_VALUE)
    right = random.randint(MIN_VALUE , Max_VALUE)
    oprators = random.choice(OPRATORS)

    expr = str(left) + " " + oprators + " " + str(right)
    answer  = eval(expr)
    return expr , answer

wrong = 0
input("Press enter to Start!")
print("--------------------------")

start_time = time.time()


for i in  range(total_problem):
    expr , answer = problem_generator()
    while True:
        guess = input("Problem #" + str(i+ 1) + " :  " + expr + " =  ")
        if  guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time , 2)

print("-----------------------")
print("Nice Work! you finished in " , total_time , " seconds!")
