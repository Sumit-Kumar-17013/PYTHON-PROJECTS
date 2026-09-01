a = float(input("Enter The First Side = "))
b = float(input("Enter The Second Side = "))
c = float(input("Enter The Third Side = "))

if(a == b and b == c and c == a):
    print("It's Equilateral Triangle")
elif(a == b or b == c or c == a):
    print("It's Isosceles Triangle")
elif(a != b and b != c and c != a):
    print("It's Scalene Triangle")
else:
    print("Not Valid!!")