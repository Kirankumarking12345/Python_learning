n=5555555
x=0
y=0
temp=n
while(0<n):
    y=y%10
    x=x*10+y
    n=n//10
print(x)
if temp==x:
    print("it is a palindrome")
else:
    print("it is not a paloindrome")
