a = float(input("Enter The First Number = "))
b = float(input("Enter The Second Number = "))
oprator = input("Enter The oprator[+ , - , * , /] = ")

match oprator:
    case "+":
        print("Result = " , a+b )
        
    case "-":
        print("Result = " , a-b)

    case "*":
        print("Result = ", a*b)
    
    case "/":
        print("Result = ", a/b )
    
    case _:
        print("Invalid!!!!")