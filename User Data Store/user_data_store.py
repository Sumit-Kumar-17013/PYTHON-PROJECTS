
def viwe():    
    pass
#     with open("USER DATA.txt" 'r') as f:
#         for line in f.read.line():


def add():
    Name = input("Enter Your First Name")
    L_name= input("Enter Your Last Name")
    # F_name = print(input("Enter Your Father Name"))
    # M_name = print(input("Enter Your Mother Name"))
    # DOB = print(input("Enter Your Date of Birth"))
    # MOb = print(input("Enter Your Mobile Number"))
    # user_name = print(input("Enter Your User-Name"))
    # Passw = print(input("Enter Your Password"))

    with open("C:\\Users\\sumit\\OneDrive\\Desktop\\Python\\Projects\\[06] User Data Store\\data.txt" , 'a' ) as f:
        f.write(Name + L_name) 

while True:
    user = input("Do You Want To Store Your Data[yes or no] & Viwe Your Data? : \n")
    if user == "no":
        break
    elif user == "yes":
        add()
    elif user == "viwe":
        viwe()
    else:
        print("Not Valid!")    