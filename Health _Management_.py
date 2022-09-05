import datetime


def gettime():
    return datetime.datetime.now()


def take(k):
    if k == 1:
        c = int(input('\nEnter 1 for Exercise and 2 for food : '))
        if c == 1:
            value = input('Type here: \n')
            with open('lokesh-ex.txt', 'a') as f:
                f.write(str([str(gettime())])+": "+value+"\n")
            print('Sucessfully written')
        elif c == 2:
            value = input('Type here: \n')
            with open('lokesh-food.txt', 'a') as f:
                f.write(str([str(gettime())])+':'+value+"\n")
            print('Sucessfully Written')
    elif k == 2:
        c = int(input('\nEnter 1 for Exercise and 2 for food : '))
        if c == 1:
            value = input('Type here \n')
            with open('kanha-ex.txt', 'a') as f:
                f.write(str([str(gettime())])+':'+value+"\n")
            print('Sucessfully Written')
        elif c == 2:
            value = input('Type here \n')
            with open('kanha-food.txt', 'a') as f:
                f.write(str([str(gettime())])+':'+value+"\n")
            print('Sucessfully Written')
    elif k == 3:
        c = int(input('\nEnter 1 for Exercise and 2 for food : '))
        if c == 1:
            value = input('Type here \n')
            with open('yogesh-ex.txt', 'a') as f:
                f.write(str([str(gettime())])+':'+value+"\n")
            print('Sucessfully Written')
        elif c == 2:
            value = input('Type here \n')
            with open('yogesh-food.txt', 'a') as f:
                f.write(str([str(gettime())])+':'+value+"\n")
            print('Sucessfully Written')
    else:
        print("Please enter valid input (1(lokesh),2(kanha),3(yogesh)")


def retrive(k):
    if k == 1:
        c = int(input('\n Enter 1 for exercise and 2 for food : '))
        if c == 1:
            with open('lokesh-ex.txt') as f:
                print(f.read())
        elif c == 2:
            with open('lokesh-food.txt') as f:
                print(f.read())
    elif k == 2:
        c = int(input('\nEnter 1 for exercise and 2 for food : '))
        if c == 1:
            with open('kanha-ex.txt') as f:
                print(f.read())
        elif c == 2:
            with open('kanha-food.txt') as f:
                print(f.read())
    elif k == 3:
        c = int(input('\nEnter 1 for exercise and 2 for food : '))
        if c == 1:
            with open('yogesh-ex.txt') as f:
                print(f.read())
        elif c == 2:
            with open('yogesh-food.txt') as f:
                print(f.read())


print('\n Welcome to Health Management System \n')
a = int(input(' Press 1 for log the value and 2 for retrive : '))
if a == 1:
    b = int(input('\nPress 1 for lokesh 2 for kanha 3 for yogesh : '))
    take(b)
else:
    b = int(input('\n Press 1 for lokesh 2 for kanha 3 for yogesh : '))
    retrive(b)
