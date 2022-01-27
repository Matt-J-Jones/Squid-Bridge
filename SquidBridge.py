import random

def bridgeRun(NumberOfPlayers, NumberOfSteps):
    Loop = True
    stepN =  1
    glass = ["Strong", "Breakable"]
    while Loop:
        if NumberOfPlayers != 0:
            GlassStep = random.choice(glass)
            if GlassStep == "Breakable":
                NumberOfPlayers = NumberOfPlayers - 1
                if NumberOfPlayers == 0:
                    Loop = False
                    x = "Everyone Died!"
            elif GlassStep == "Strong":
                pass
            stepN = stepN + 1
            NumberOfSteps = NumberOfSteps - 1
            if NumberOfSteps == 0:
                if NumberOfPlayers == 0:
                    x = "Everyone Died!"
                else:
                    x = str(NumberOfPlayers) + " Survived!"
                Loop = False
    return x

count = 0
count2 = 0
x = " "
steps = 18
players = input("Enter Number of Players: ")
players = int(players)

if players > steps:
    print("Error, number of players needs to be lower than number of steps")
    quit()

while x != "1 Survived!":
    x = bridgeRun(players, steps)
    count = count + 1

print(count, " cycles for exactly 1 survivor")
