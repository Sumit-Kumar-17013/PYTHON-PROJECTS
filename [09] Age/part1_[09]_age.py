age = int(input("Enter Your Age = "))

if(age >= 60 and age < 120):
    print("Senior")

elif( age >= 18 and age < 60):
    print("Adult")

elif(age >= 13 and age < 18):
    print("Teen")

elif(age >= 1 and age < 13):
    print("Child")

else:
    print("Not Valid")