import random

def gen_pass():
    num = int(input("Enter a number: "))
    password = " "
    for i in range(num):
        r = random.randint(65,90)
        letter = chr(r)
        password = password + letter
    print("Password:" + password)

gen_pass()