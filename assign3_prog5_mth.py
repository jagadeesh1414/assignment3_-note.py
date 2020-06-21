a=int(input("enter a value"))
b=int(input("enter b value"))
c=int(input("enter c value"))
def maximum(a, b, c):  
    if (a > b) and (a > c): 
        largest = a 
        print("a is largest")
  
    elif (b > a) and (b > c): 
        largest = b 
        print("b is largest")
    else: 
        largest = c 
        print("c is largest")
    return largest   
print(maximum(a, b, c))
