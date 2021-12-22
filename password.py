import random 

passwordLength = 24
password = []

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
digitsList = ['0','1','2','3','4','5','6','7','8','9']
specialList = ['@','#', '$', '%', '&' ,'_', '?','.','*']

while True:
    letters_upper = random.randrange(2,6)
    letters_lower = random.randrange(8,13)
    special = 3
    digits = random.randrange(4,7)

    total = letters_lower + letters_upper + special + digits
    if total == passwordLength:
        break

for x in range (letters_upper):
    choices = random.choice(letters)
    password.append(choices)

for b in range (letters_lower):
    choices = random.choice(letters)
    password.append(choices.lower())

for m in range(special):
    choices = random.choice(specialList)
    password.append(choices)

for l in range(digits):
    choices = random.choice(digitsList)
    password.append(choices)  

while True:
    random.shuffle(password)

    if password[0] in digitsList or password[1] in digitsList or password[2] in digitsList or password[0] in specialList or password[23] in specialList:
        None
    else:
        break
print(''.join(password))
    