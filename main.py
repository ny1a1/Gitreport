from time import sleep
from random import randint
from datetime import datetime

list = [2, 4, 6, 8, 10]
c = randint(1,11)
for i in range(randint(1, 15)):
    a = randint(1, 10)

    if a == 10:
        print("Hello World!")
    elif a == 9:
        print("Hello Jhon!")
    elif a == 8:
        print("Hi James!")
    elif a == 5:
        print("Hello, it's United States of America!")
    elif a == 2:
        print("Hello Git!")
    else:
        print("Bay!")
    sleep(1)

print("Text")
print("Text 222")
print(datetime.today())
if c in list:
    print("Omg!")
else:
    print("Hello Ukrainian people!")