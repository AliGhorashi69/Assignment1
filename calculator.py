import math

cos=math.cos
sin=math.sin
tan=math.tan
sqrt=math.sqrt
fact=math.factorial
pi=math.pi


M=input("Do you want comput sinosoidal functions? (Yes or No): ")

if M=="Yes":
    x=float(input("Please enter a number: "))
    S=input("Is this parameter based on degree (Yes or No): ")
    if S=="No":
        x=180/pi

op=input("please select an operation, (Insert: cos for cosinous, sin or sinous, tan for tangant, sqrt for squared root, fact for factorial")
y=0
if op=="cos":
    y= cos(x)
if op=="sin":
    y=sin(x)
if op=="tan":
    if cos(x)==0:
        print("Error, Division by zero ")
    else :
        y=tan(x)
if op=="cot":
    if sin(x)==0:
        print("Error, Division by zero")
    else:
        y=1/tan(x)
if op=="fact":
    y=fact(x)
if op=="sqrt":
    if x<0:
        print("Error, Not a real number")
    else:
        y=sqrt(x)
else: 
  print("not a valid function")


print("These result is: ", y)



