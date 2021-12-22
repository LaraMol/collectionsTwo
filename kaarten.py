import random

kleuren = ['harten' , 'klaveren' , 'schoppen' , 'ruiten']
kaarten = ['2','3','4','5','6','7','8','9','10','boer','vrouw','heer','aas']

deck = []
for x in kleuren:
    for y in kaarten:
        kaart = f"{x} {y}"
        deck.append(kaart)
for a in range(2):  
    deck.append('joker')


random.shuffle(deck)

for b in range(7):
    kaart = random.choice(deck)
    deck.remove(kaart)
    print(kaart)


print(deck)
