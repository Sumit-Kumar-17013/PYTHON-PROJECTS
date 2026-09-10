name = str(input("Enter Your Name: "))
print("Welcome to Adventure Game" , name , "!.")

person = input("When you are in Dehri On Sone, How will you go Sasaram? 'bus, auto, train' ?").lower()

if person == "train":
    person = input("Good Chooise , Then When You reach Sasaram , How will you goo Village? 'bus , auto'? ")

    if person == "bus":
        person = input("Good Chooise , Then When You reach Main Gate Of Village , How will you goo Home? 'walk , auto'? ")
       
        if person == "walk":
            person = input("Congratulation! Finelly You Reached , Then What are doing Here 'study , fun ?")
           
            if person == "fun":
                print("So Fun , Thanks To play This Game" )
            elif person == "study":
                print("Sorry you Lost , cuz It's weekend")
            else:
                print("Not Valid!")

        elif person == "auto":
            print("Sorry you Lost , cuz Not Facility For auto.")
        else:
            print("Not Valid!")
   
    elif person == "auto":
        print("Sorry you Lost , Not Avalible Any time. ")
    else:
        print("Not Valid!")

elif person == "bus":
    person = input("Sorry you Lost , cuz Very Expensive ")

elif person == "auto":
    print("Sorry you Lost , cuz Very Expensive ")
else:
    print("Not Valid!")


print("----GAME OVER----")