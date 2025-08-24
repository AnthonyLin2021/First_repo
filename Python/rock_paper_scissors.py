


import random

print ("===================")
print ("Rock Paper Scissors")
print ("===================")



player=int(input("Pick a number:\n1 is for '✊' (Rock).\n2 is for '✋' (Paper).\n3 is for '✌️' (Scissors).\n"))


computer=random.randint(1,3)

if player ==1:
    print("You chose ✊")
    if computer ==1:
        print("CPU chose ✊\nIt's a tie!")
    elif computer ==2:
        print("CPU chose ✋\nYou lost!")
    else:
        print("CPU chose ✌️\nYou won!")
elif player ==2: 
    print("You chose ✋")
    if computer ==1:
        print("CPU chose ✊\nYou won!")
    elif computer ==2:
        print("CPU chose ✋\nIt's a tie!")
    else:
        print("CPU chose ✌️\nYou lost!")
elif player ==3: 
    print("You chose ✌️")
    if computer ==1:
        print("CPU chose ✊\nYou lost!")
    elif computer ==2:
        print("CPU chose ✋\nYou Won!")
    else:
        print("CPU chose ✌️\nIt's a tie!")
