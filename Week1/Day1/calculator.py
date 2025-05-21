x = float(input("Enter First Number: "))
y = float(input("Enter Second Number: "))
operator = input('Enter ( +,-,*,/,%,//: ): ') 

if operator == "+":
    print(f"Sum of {x} and {y} is : {x+y}")
elif operator == "-":
    print(f"Difference of {x} and {y} is : {x-y}")
elif operator == "*":
    print(f"Multiplication of {x} and {y} is : {x*y}")
elif operator == "/" :
    print(f"Division of {x} and {y} is : {x/y}")
elif operator =="%":
    print(f"Remainder of {x} and {y} is : {x%y}")
elif operator =="//":
    print(f"floorDivision of {x} and {y} is : {x//y}")
else:
    print("Enter Correct Operator" )