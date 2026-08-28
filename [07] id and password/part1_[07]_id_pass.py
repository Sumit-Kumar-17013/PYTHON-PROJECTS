username = "python"
password = "Pass123@"

user = str(input("Enter The Username = "))
user2 = str(input("Enter The Password = "))

if (user == username and user2 == password):
    print("Login Complete!")
else:
    print("Login Failed")