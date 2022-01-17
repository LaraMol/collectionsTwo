import random

Dobbelstenen = ['1','2','3','4','5']
listbfilled = [' '] * 6
listbScores = [' '] * 6

def printResultaten(listbScores):
    print(f"""Totaal resultaten van allen 1's: {listbScores[0]} 
Totaal resultaten van allen 2's: {listbScores[1]} 
Totaal resultaten van allen 3's: {listbScores[2]} 
Totaal resultaten van allen 4's: {listbScores[3]} 
Totaal resultaten van allen 5's: {listbScores[4]} 
Totaal resultaten van allen 6's: {listbScores[5]} """)

def printBovenste(listbfilled):
    print (f"""---------------------------------------------
ENEN                  |{listbfilled[0]} 
TWEEËN                |{listbfilled[1]} 
DRIEËN                |{listbfilled[2]} 
VIEREN                |{listbfilled[3]} 
VIJFEN                |{listbfilled[4]} 
ZESSEN                |{listbfilled[5]}
---------------------------------------------""")

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

def loop(listbfilled):
    if ' ' in listbfilled:
        return True
    else:
        return False


while loop(listbfilled):
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
    printResultaten(listbScores)

    while True:
        invulAntwoord = int(input("Welk getal wil je invoeren?: "))
        if listbfilled[(invulAntwoord - 1)] != ' ':
            print('Dat is al ingevuld!')
        else: 
            listbfilled[(invulAntwoord - 1)] = listbScores[(invulAntwoord - 1)]
            break

    printBovenste(listbfilled)
