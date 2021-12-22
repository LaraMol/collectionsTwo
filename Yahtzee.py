import random

Dobbelstenen = ['1','2','3','4','5']
scoreboard = []
pogingen = 2

def rolledDice(Dobbelstenen):
    for x in range(len(Dobbelstenen)):
        Dobbelstenen[x] = random.randint(1,6)
    return Dobbelstenen 

def printDice(Dobbelstenen):
    for x in range(len(Dobbelstenen)):      
        print(f"Dobbelsteen:{x + 1} = {Dobbelstenen[x]}")

rolledDice(Dobbelstenen)
printDice(Dobbelstenen)