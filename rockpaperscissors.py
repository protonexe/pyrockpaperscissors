import random
def tie(input,computer):
    if input==computer:
        return f"Computer picks {computer}, Tie" 
ch="y"
wins=0
losses=0
ties=0
rounds=0
po=["Rock","Paper","Scissors"]
print("Welcome to Rock Paper Scissors!")
while ch=="y":
    
    pl=input("Enter your choice:")
    co=random.choice(po)
    pl=pl.lower()
    valid=["rock","r","paper","p","scissors","s"]
    if pl not in valid:
        print("Invalid Input!")
        continue
    if pl in ["r","rock"]:
        pl="Rock"
    elif pl in ["p","paper"]:
        pl="Paper"
    elif pl in ["s","scissors"]:
        pl="Scissors"
    label=tie(pl,co)
    if label!=None:
        print(label)
        ties+=1
    else:
        if pl=="Rock" and co=="Paper":
            print("Computer picks Paper, Computer Wins")
            losses+=1
        elif pl=="Rock" and co=="Scissors":
            print("Computer picks Scissors, You Win!")
            wins+=1
        elif pl=="Paper" and co=="Rock":
            print("Computer picks Rock , You Win!")
            wins+=1
        elif pl=="Paper" and co=="Scissors":
            print("Computer picks Scissors , Computer Wins")
            losses+=1
        elif pl=="Scissors" and co=="Rock":
            print("Computer picks Rock , Computer Wins")
            losses+=1
        elif pl=="Scissors" and co=="Paper":
            print("Computer picks Paper , You Win!")
            wins+=1
    print("Score-",wins,"Wins |",losses,"Losses |",ties,"Ties")
    rounds+=1
    ch=input("Continue? (y/n)")
if rounds > 0:
    print(f"\nFinal Stats-\nWins {wins} | Losses {losses} | Ties {ties} \nWin Percentage=",int((wins/(wins+losses+ties))*100),"% \nTotal Rounds=",rounds,sep="")
else:
    print("No valid rounds were played!")




    
    