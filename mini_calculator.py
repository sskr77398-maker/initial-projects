''' small calculator for only (+-*/)'''

operator = input("enter operator (+ - * /): ")

number1 = float(input("enter num1: "))
number2 = float(input("enter num2: "))

if operator == "+":
    print(round(number1+number2, 2))
elif operator == "-":
    print(round(number1-number2, 2))
elif operator == "*":
    print(round(number1*number2, 2))
elif operator == "/":
    print(round(number1/number2, 2))   
else:
    print("invalid operator")          
    