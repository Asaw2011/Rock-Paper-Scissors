from random import choice
game="rock","paper","scissor"
while True:
    cs=0
    us=0
    rounds=int(input("How many rounds do you want to play: "))
    chances=rounds
    for i in range(rounds):
        computer=choice(game)
        user=input("Hello enter rock paper or scissor: ")
        print("computer:",computer)
        print("user:",user)


        if(computer==user):
            print("draw")

        elif(computer=="rock"):
            if(user=="paper"):
                print("You won")
                us+=1
            else:
                print("You lose")
                cs+=1
        elif(computer=="paper"):
            if(user=="scissor"):
                print("You won")
                us+=1
            else:
                print("You lose")
                cs+=1
        else:
            if(user=="rock"):
                print("You won")
                us+=1
            else:
                print("You lose")
                cs+=1
        chances-=1
        print("----------------")
        print("computer score",cs)
        print("user score",us)
        print("rounds remaining =",chances)
        print("----------------")

    if(us>cs):
        print("You won")
    elif(cs>us):
        print("You lost")
    else:
        print("Its a tie")

    stop=input("Print yes if you want to stop, other wise type anything else it does not matter")
    if(stop=="yes"):
        break
    else:
        continue
print("Thanks for playing")