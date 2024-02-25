

import time


def count_down_from(second):
    for i in range(second, 0, -1):
        time.sleep(1)
        print(i,)

print("-------------------------")
print("LETS GOOOOOOOOOOOOOOOOO!")

count = 0
in_exercise = 0
if int(input("Ready to exercise?: 1. Lets GOOOO   2.Not today\n")) == 1:
    in_exercise = 1
else:
    print("NOOOOOOO LETS DO IT!!!!")
    if int(input("1. hmmm ok   2.nahh\n")) == 1:
        in_exercise = 1
    else:
        print("NOOOOO you dont want to lose your streak!!!")
        if int(input("1. oh shit lets get it   2. get off I want to lose my streak\n")) == 1:
            in_exercise = 1
            print("Lets fucking goooooooooooooooo")
        else:
            print("bye loser")
            if int(input("1. fuck let me do it\n")) == 1:
                in_exercise = 1

if(in_exercise == 1):
    print("Ready?")
    in_exercise = 1
    number_today = []
    count_down_from(3)
    time.sleep(2)
    while(in_exercise == 1):
        print("-------------------------")
        count = input("How many you did this set?\n")
        number_today.append(count)
        time.sleep(1)
        print("niceeeeeeeeeeeeeeeeeee")
        time.sleep(1)
        if(int(input("Ready for another set? 1. Keep going  2. Call it a day \n")) == 2):
            in_exercise = 0
        else:
            print("eeee lets get it")
        time.sleep(3)
    print("-------------------------")
    print("total number completed today", sum(map(int, number_today)))




















