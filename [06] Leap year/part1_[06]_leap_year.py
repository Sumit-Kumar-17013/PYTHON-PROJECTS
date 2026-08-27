user = int(input("Enter the Year = "))

if(user % 400 == 0 and user % 100 == 0):
    print("It's Leap Year!!!")
elif(user % 4 == 0  and user % 100 != 0):
    print("It's leap Year!!!")
else:
    print("Not Leap Year!!!")
