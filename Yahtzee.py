import random

Dobbelstenen = ['1','2','3','4','5']
scoreboard = []
listbfilled = [' '] * 6
listbScores = [' '] * 6
pogingen = 2

def upperHalfScore(Dobbelstenen:list):
    howManyDigits = []
    for digit in range(1,7):
        howManyDigits.append(Dobbelstenen.count(digit))
    listUpperHalf = []
    for z in range(0,6):
        x = howManyDigits[z] * (z + 1)
        listUpperHalf.append(x)
    return listUpperHalf

def rolledDice(Dobbelstenen):
    for x in range(len(Dobbelstenen)):
        Dobbelstenen[x] = random.randint(1,6)
    return Dobbelstenen 

def printDice(Dobbelstenen):
    for x in range(len(Dobbelstenen)):      
        print(f"Dobbelsteen:{x + 1} = {Dobbelstenen[x]}")

def reroll(listRerolls,Dobbelstenen):
    for x in listRerolls:
        position = x -1
        roll = random.randint(1,6)
        Dobbelstenen[position] = roll
    return Dobbelstenen

rolledDice(Dobbelstenen)
printDice(Dobbelstenen)

pogingen = 2
while pogingen != 0:
    rerollVraag = input(f"Wilt u rerollen? U heeft nog {pogingen} pogingen (Y/N) ")
    if rerollVraag.lower() == "y":
        listRerolls = []
        while True:
            inputReroll = int(input("Welke dobbelstenen moeten opnieuw gerolled worden? (0 is done): "))
            if inputReroll != 0:
                listRerolls.append(inputReroll)
            else:
                break
        Dobbelstenen = reroll(listRerolls,Dobbelstenen)
        printDice(Dobbelstenen)
        pogingen -= 1
    elif rerollVraag.lower() == "n":
        break
    else:
        print("Dat is geen optie")

listbScores = upperHalfScore(Dobbelstenen)
print (listbScores)

BovensteScore = f"""---------------------------------------------
ENEN                  |{listbScores[0]} 
TWEEËN                |{listbScores[1]} 
DRIEËN                |{listbScores[2]} 
VIEREN                |{listbScores[3]} 
VIJFEN                |{listbScores[4]} 
ZESSEN                |{listbScores[5]}
---------------------------------------------"""
