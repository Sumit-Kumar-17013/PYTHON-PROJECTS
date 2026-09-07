import random
guess = random.randint(1 , 100)
guessess = 0

while True:
    guessess += 1
    userchoise = input("Guess The Number Between '1 to 100' or 'Quit' \n")
    if (userchoise == "Quit"):
        break
        
    userchoise = int(userchoise)

    if (userchoise == guess):
        print("Correct! Guess")
        break
    elif(userchoise < guess):
        print("Its too 'Small',  Guess Bigger Than Pervious! ")    
    else:
        print("Its Too 'Bigg' , Guess Smaller Than Pervious! ")    

print("You Got it in" , guessess ,"Moves")
print("(:-----GAME OVER----- :)")