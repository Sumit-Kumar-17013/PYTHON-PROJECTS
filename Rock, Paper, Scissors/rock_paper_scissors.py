import random

user_win = 0
computer_win = 0
drow = 0

option = ["rock", "paper" , "scissor"]
while True:
    user_number = input("Enter [rock , paper , scissor] OR Quit [q]. \n").lower()
    if user_number == "q":
        break

    if user_number not in option:
        continue

    random_number = random.randint(0 ,2)
    #Rock = 0, paper = 1, scissor = 2 
    computer_user = option[random_number]
    print("Computer Picked" , computer_user + ".")

    if (user_number == "rock" and computer_user == "scissor"):
      print("You Won!")
      user_win += 1

    elif (user_number == "scissor" and computer_user == "paper"):
      print("You Won!")
      user_win += 1

    elif (user_number == "paper" and computer_user == "rock"):
      print("You Won!")
      user_win += 1

    elif (user_number == "rock" and computer_user == "rock"):
       print("DROW !")
       drow += 1

    elif (user_number == "paper" and computer_user == "paper"):
       print("DROW !")
       drow += 1

    elif (user_number == "scissor" and computer_user == "scissor"):
       print("DROW !")
       drow += 1
       
    else:
      print("You Lost! , Computer Win")
      computer_win += 1

print(" \n    --RESULT--    \n")
print("You won " , user_win , "times. \n")
print("Computer Won" , computer_win , "times. \n") 
print("Drow" , drow , "times. \n")
print("Game Over :) \n")
