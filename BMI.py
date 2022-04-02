w=float(input("Please enter your weight (in Kg): "))
h=float(input("Please enter your height (in cm): "))

if (h>250 or h<50) and (w>200 or w<10):
    print ("It seems you enter wrong numbers")
    w=float(input("Please enter your weight again (in Kg): "))
    h=float(input("Please enter your height again (in cm): "))

BMI=w/((h/100)**2)

if BMI<=18.5:
    print("Your BMI is: ", BMI, "and you are underweight")

if 18.5<BMI<=25:
    print("Your BMI is: ", BMI, "and you are normal")
if 25<BMI<=30:
    print("Your BMI is: ", BMI, "and you are overweight")
if  30<BMI<=35:
    print("Your BMI is: ", BMI, "and you are obese")
if BMI>35:
    print("Your BMI is: ", BMI, "and you are extremly obese")
