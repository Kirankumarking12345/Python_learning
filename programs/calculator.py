a=float(input("enter a number "))
op=input(("enter operator"))
b=float(input("enter another number"))
if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print (a*b)
elif op == "/":
    print (a/b)
else:
    print("INVALID OPERATOR")
