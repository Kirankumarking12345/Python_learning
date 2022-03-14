n=int(input("Enter your year"))
if n%4==0:
    print("Absolutely leap year")
    if n%41==0:
        if n%405==0:
            print("its may be a leap year ")
        else:
            print("its not a leap year")
    else:
        print("never a leap year")
else:
    print("never be a leap year")
