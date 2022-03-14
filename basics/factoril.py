#factorial
n=int(input("enter a number"))
a=0
b=1
while a<n:
      a=a+1
      b=a*b
print("factoril is",b)


#for loop factorial
a = int(input('a='))
b = 1
for c in range(1,a+1):
      b = b*c
print(b)



#to find big one in3 no
a = int(input('a ='))
b = int(input('b='))
c = int(input('c='))
if a>b and a>c:
      print('a is big')
elif b>a and b>c:
      print('b is big')
else:
      print('c is big')


# to find a no is a perfect  no:
a = int(input('a ='))
c = 0
for b in range(1,a):
      if a%b == 0:
            c = c+b
if a == c:
      print('pERFECT')




      

      

