print ("--------------------")
print ("|   Calculator       |")
print ("| [1] Sum            |")
print ("| [2] Subtraction    |")
print ("| [3] Multiplication |")
print ("| [4] Division       |")
print ("--------------------")

opt = int(input("Enter one option: "))

match opt:
    case 1: 
        print ("Sum")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print ("Result: ", num1 + num2)
    case 2: 
        print ("Subtraction")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print ("Result: ", num1 - num2)
    case 3: 
        print ("Multiplication")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print ("Result: ", num1 * num2)
    case 4: 
        print ("Division")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print (f"Result: {num1/num2:.2f} ")
