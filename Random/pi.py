import os
from decimal import *
getcontext().prec=100
file = open('pi.txt', 'w')
counter = 1
pi = 3
x = 2
while counter < 10000000:
    if counter % 2 == 1:
        pi = Decimal(pi) + Decimal(4) / Decimal((x * (x + 1) * (x + 2)))
    else:
        pi = Decimal(pi) - Decimal(4) / Decimal((x * (x + 1) * (x + 2)))
    counter = counter + 1
    x = x + 2
    os.chdir("C:\\Users\\cooperb7\\Desktop")
    file.write(str(pi) + "\r\n")
    #print(pi)
file.close()