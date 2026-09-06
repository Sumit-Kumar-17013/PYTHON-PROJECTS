print("Welcome To My Computer Quiz")

playing = (input("Do You Want To Play?\nIf You Want To Then Enter [yes] , Other wise [no]\n"))
if playing.lower() != "yes":
    quit()

print("Okay! Let's Play :)")
score = 0

question1 = input("1. What Does 3+3? \n")
if (question1.lower() == "6"):
    print("Correct!")
    score += 1 
else:
    print("Incorrect")  

question2 = input("2. What Does 8+8? \n")
if (question2.lower() == "16"):
    print("Correct!")
    score += 1 
else:
    print("Incorrect")

question3 = input("3. What Does 3*3? \n")
if (question3.lower() == "9"):
    print("Correct!")
    score += 1 
else:
    print("Incorrect") 

question4 = input("4. What Does5*5? \n")
if (question4.lower() == "25"):
    print("Correct!")
    score += 1 
else:
    print("Incorrect")

question5 = input("5. What Does 3*4? \n")
if (question5.lower() == "12"):
    print("Correct!")
    score += 1 
else:
    print("Incorrect")

question6 = input("6. What Does 2+2? \n")
if (question6.lower() == "4"):
    print("Correct!")
    score += 1 
else:
    print("Incorrect") 

question7 = input("7. What Does 3*8? \n")
if (question7.lower() == "24"):
    print("Correct!")
    score += 1 
else:
    print("Incorrect")


question8 = input("8. How Many Chammber In Heart? \n")
if (question8.lower() == "4" ):
    print("Correct!")
    score += 1 
else:
    print("Incorrect")                   

question9 = input("9. How Many Bones In Human ? \n")
if (question9.lower() == "206"):
    print("Correct!")
    score += 1 
else:
    print("Incorrect")     


question10 = input("10. What Does Supply Volatge in Elecrtic Power Plant? \n")
if (question10 == "440"):
    print("Correct!")
    score += 1 
else:
    print("Incorrect")    


print("You Got " + str(score) + " Question Correct Out Of '10' Question.")
print("You Got " + str((score/10) * 100) + "%.")
