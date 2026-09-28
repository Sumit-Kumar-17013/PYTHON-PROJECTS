import random

print("Welcome To HangMan Game..!")
words = ["BIHAR" , "ARUNACHALPRADESH" ,"HARYANA" ,"NAGALAND" , "UTTARAKHAND" , "MIZORAM" , "MANIPUR" , "GOA" ,]
word = random.choice(words)

total_chance = 10
guesss_word = "_"*len(word)

while total_chance !=0:
    print(guesss_word)
    letter = input("Guess The state Name...:) ").upper()
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guesss_word = guesss_word[:i]+letter+guesss_word[i+1:]
        if guesss_word == word:
            print("Congratulations You Win..!!")
            break
    else:
        total_chance -= 1
        print("Incorrect Guess.")
        print("Remaining Life Left " , total_chance)``
else:
    print("You Loss..!!!!\nGame Over \nNo Left Life")
print("The Correct Word Is" , word)

