First=input("Please enter your first name: ")
Last=input("Please enter your last name: ")

score1=float(input())
if score1<0 or score1>20:
    print("The score should be number between 0 to 20")
    score1=float(input("Please enter the score again"))


score2=float(input())
if score2<0 or score2>20:
    print("The score should be number between 0 to 20")
    score2=float(input("Please enter the score again"))


score3=float(input())
if score3<0 or score3>20:
    print("The score should be number between 0 to 20")
    score3=float(input("Please enter the score again"))

score4=float(input())
if score3<0 or score3>20:
    print("The score should be number between 0 to 20")
    score4=float(input("Please enter the score again"))

avg=(score1+score2+score3+score4)/4

if (avg < 12):
    print("Hi", First,"", Last, 'Your average is:', avg, 'FAIL !')
    
elif (avg >= 12 and avg < 17):
    print("Hi", First,"", Last, 'Your average is:', avg, 'Normal ...')
    
else:
    print("Hi", First,"",Last, 'Your average is:', avg, '. You are great :)')