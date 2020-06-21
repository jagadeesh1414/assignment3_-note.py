a=int(input("enter 1st input"))
b=int(input("enter 2nd input"))
c=int(input("enter 3rd input"))
if a==b and b==c:
    print("three inputs are equal")
elif a==b or b==c:
    print("any two are equal")
elif c==a:
    print("any two are equal")