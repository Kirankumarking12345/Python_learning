#nested if
n=int(input("enter a number"))
if n<100:
    print("its less than 100")
    if n%2==0:
        print("its an even number")
        if n<50:
            print("its less than 50 and its an even")
        else:
            print("its greater than 50 and its an even")
    else:
        print("it is an odd number")
else:
    print("it is greater than 100")

#for loop
a=int(input("a="))
b=1
for c in range(1,a+1):
    b=b*c
print(b)

#finding big one
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

if a>b and a>c:
    print("a is big")
elif b>a and b>c:
    print("b is big")
else:
    print("c is big")

#swapping of number
a = int(input("a="))
b = int(input("b="))
a = a+b
b = a-b
a = a-b
print("a=",a,"b=",b)

#another swapping
a =int(input("enter a number"))
b =int(input("enter a number"))
c= a
a= b
b= c
print(a,b)

