import random

response = input("Do you want to roll the dice?")

if(response == "yes"):
 while(response == "yes"):
    no = random.randint(1,6)
    if(no == 1):
        print("[$$$$$]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[$$$$$]")
    if(no == 2):
        print("[$$$$$]")
        print("[     ]")
        print("[ 0  0]")
        print("[     ]")
        print("[$$$$$]")
    if(no == 3):
        print("[$$$$$]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[$$$$$]")
    if(no == 4):
        print("[$$$$$]")
        print("[  0  ]")
        print("[0  0 ]")
        print("[  0  ]")
        print("[$$$$$]")
    if(no == 5):
        print("[$$$$$]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[$$$$$]")
    if(no == 6):
        print("[$$$$$]")
        print("[ 0 0 ]")
        print("[ 0 0 ]")
        print("[ 0 0 ]")
        print("[$$$$$]")

    response = input("Do you want to roll the dice?")
if(response == "no"):
    print("E Tu Ja Re")