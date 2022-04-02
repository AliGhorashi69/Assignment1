a=float(input("enter the a: "))
b=float(input("enter the b: "))
c=float(input("enter c: "))

if a>b+c or b>a+c or c>a+b:
    print ("It is not possible to draw a triangle with these features")
else :
    print("These parameter can form a triangle")