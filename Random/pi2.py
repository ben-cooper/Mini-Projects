import os
from decimal import *
def ask_user():
    precision = input("# of pi digits to calculate: ")
    if input("Would you like to output (y/n): ") == "y":
        output = True
        path = input("Path to output: ")
    else:
        output = False
        path = None
    return calc_pi(precision,path,output)
def calc_pi(precision,path,output):
    try:
        getcontext().prec=int(precision) + 4
        if path != None:    
            os.chdir(path)
    except:
        ask_user()
    else:
        file = open('pi.txt', 'w')
        counter = 1
        pi = 3
        x = 2
        old = 0
        while pi != old:
            if counter % 3 == 2:
                old = pi
            if counter % 2 == 1:
                pi = Decimal(pi) + Decimal(4) / Decimal((x * (x + 1) * (x + 2)))
            else:
                pi = Decimal(pi) - Decimal(4) / Decimal((x * (x + 1) * (x + 2)))
            counter = counter + 1
            x = x + 2
            result = str(pi)
            result = result[:int(precision)+1]
            os.system('cls')
            print(result)
            if output:
                file.write(result + "\r\n")
        file.close()                   
        return result
if __name__ == "__main__":
    os.system('title Pi Calculator')
    print(ask_user())
    os.system('pause')