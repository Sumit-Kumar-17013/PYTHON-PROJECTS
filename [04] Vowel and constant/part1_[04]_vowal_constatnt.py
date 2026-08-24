vowel = ['a', 'e' , 'i ', 'o' ,'u']
constant = ['b' , 'c' ,'d' , 'f' , 'j' , 'k' ,'l' ,'m', 'n' , 'p' , 'q','r' ,'s' , 't' ,'v' , 'w' , 'x' , 'y', 'z' ]

user = str(input("Enter The Alphabet = "))

user = user.lower()

if(user in vowel):
    print("It's Vowel")
elif(user in constant):
    print("It's Constant")
else:
    print("Not Valid!!!")