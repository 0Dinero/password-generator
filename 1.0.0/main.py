import time
import os
from random import randint
from random import seed
def randomgen(num):
    counter = 1
    password = ""
    letters = ["A","b","C","d","E","f","G","h","!","12","1","2","3","4","5","6","7","8","9","10"]
    while counter <= num:
        time.sleep(0.1)
        seed()
        x = randint(0, 19)
        i = letters[x]
        xx = str(i)
        password += xx
        counter +=1
    print(password)
print("Welcome to my password-generator")
i = input("How many characters do you want your password to contain?: ")
ii = int(i)
if ii <= 0:
    exit()
else:
    print("Please wait a few seconds while we generate your password...")
    randomgen(ii)
    os.system("pause")