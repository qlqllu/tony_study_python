import random
import time

def pandablow(things):
    match things:
        case 1:
            return('fire')
        case 2:
            return('lava')
        case 3:
            return('lightning')
        case 4:
            return('liquid helium')
        case 5:
            return('laser')


while True:
    x =random.randint(0,5)
    y = pandablow(x)
    print(y)
    time.sleep(0.7)

