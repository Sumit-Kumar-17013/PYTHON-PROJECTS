side1 = float(input("Enter The First Side = "))
side2 = float(input("Enter The Second Side = "))
side3 = float(input("Enter The Third Side = "))

if(side1 + side2 +side3 == 180 and side1 > 0 and side2 > 0 and side3 > 0):
    print("Valid Triangle")
else:
    print("Not Valid")