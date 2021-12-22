producten = []
hoeveelProducten = []
while True:
    Product =input('Wat wilt u in uw boodschappenlijstje toevoegen: ')
    if Product.lower() == 'stop':
        break
    elif Product in producten:
        Waar = producten.index(Product)
        hoeveelProducten[Waar] += 1 
    else:
        producten.append(Product)
        Hoeveel = int(input('Hoeveel wilt u van dit product: '))
        hoeveelProducten.append(Hoeveel)

for x in range(len(producten)):
    print(f"Product = {producten[x]} Hoeveel = {hoeveelProducten[x]}")

