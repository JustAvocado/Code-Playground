from random import *

sweets = []

sweets.append(randint(1000, 9999))

sweetCode = randint(1000, 9999)

for x in sweets:
    sweetCode = randint(1000, 9999)
    if sweets[x] == sweetCode:
        break
    else:
        sweets.append(sweetCode)


for i in sweets:
    print(i)
