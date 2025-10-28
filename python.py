import random


print("Enter level: \n 1)range 1-10 \n 2)range 1-50 \n 3) 1-100")

def lvl(min_num,max_num):
    ran= random.randint(min_num,max_num)
    count=0
    while count!=3:
        ans=int(input("enter your guess"))
        count+=1
        if ans==ran:
            print("Correct")
            break
        elif ans>ran:
            print("High")
        elif ans<ran:
            print("low")
    else:
        print("You lost: the guess was "+ str(ran))

r=int(input("enter the level:"))
if r==1:
    lvl(1,10)
elif r==2:
    lvl(1,50)
elif r==3:
    lvl(1,100)
else:
    print("Invalid")
