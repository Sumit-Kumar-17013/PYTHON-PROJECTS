n = float(input("Enter The Marks Out Of 100 = "))

if(n >= 90 and n <=100):
    print("A+")
elif(n >= 80 and n < 90):
    print("A")
elif(n >= 70 and n < 80):
    print("B")
elif(n >= 60 and n < 70):
    print("B+")
elif(n >= 50 and n < 60):
    print("C")
elif(n >= 40 and n < 50):
    print("C+")
elif(n >= 30 and n < 40):
    print("D")
elif(n >= 20 and n < 30):
    print("D+")
elif(n >= 0 and n < 20):
    print("F")
else:
    print("Invalid Number")