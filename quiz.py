print("Welcome to my computer quiz.")
playing=input("Do you want to play? ")
if playing.lower() !="yes":
    quit()
else:
    print("Okey, let's play.")
score=0
answer=input("What is the boiling point temperature (water) in celcious? ")
if answer.lower() =="100":
    score+=1
else:
    print("incorrect")

answer=input("In which city did Diana, Princess of Wales, died? ")
if answer.lower() =="paris":
    score+=1
else:
    print("incorrect")

answer=input("What is the capital city of Australia? " )
if answer.lower() =="Canberra":
    score+=1
else:
    print("incorrect")

answer=input("Which actor played Rocky? ")
if answer.lower() =="Sylvester Stallone":
    score+=1
else:
    print("incorrect")
answer=input("Which fruit is associated with Isaac Newton? ")
if answer.lower() =="apple":
    score+=1
else:
    print("incorrect")
print("your score is " +str(score))
print("So you got "+str((score/5)*100)+"%")
print("Thanks for playing")



