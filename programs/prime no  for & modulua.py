a=2
if type(a)==float:
    print("deciimal")
else:
    print("not a decimal")
n=int(input("enter ur number"))
if n>1:
    for k in (2,n):
        if n%k==0:
            print("its not a prime")
            break
        else:
            print("its a prime")
            break
else :
    print("please enter ur number greater than 1")
