a = int(input('a='))
b = int(input('b='))
a = a+b
b = a-b
a = a-b
print('a is',a, 'b is',b)


#to find a no is a prime or not:
A = int(input('A='))
if A >1:
    for C in range(2,A):
        if A%C==0:
            print('not a prime no')
            break
        else:
            print('prime')
            break
else:
    print("enter positive number")


