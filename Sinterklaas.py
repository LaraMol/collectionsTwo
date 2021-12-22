import random

Namen = []
Lootjes = [ ]

while True:
    vraag = input ("Type hier een naam: ")
    if vraag in Namen: 
        print('Deze naam heeft u al ingevoerd')
    else:
        Namen.append(vraag)
    if len(Namen) >= 2:
        zekerheid = input ("Wilt u nog meer namen toevoegen? Y/N: ")
        if zekerheid.lower() == "n":
            break

ShuffledNamen = []
ShuffledNamen +=  Namen

random.shuffle(ShuffledNamen) 

aantal = (len(Namen) - 1)
while aantal > 0:
    if ShuffledNamen[aantal] == Namen[aantal]:
        random.shuffle(ShuffledNamen)
        aantal = (len(Namen) -1)
    else:
        aantal -= 1

namen = ''
for x in Namen:
    namen += x + ', '
shufflednamen = ''
for z in ShuffledNamen:
    shufflednamen += z + ', '
print(f"Namen = {namen}") 
print(f"Lootjes =  {shufflednamen}")