#!/usr/bin/env/python3

import time

print(r"""

 _____                     _                __                       
| ____|___  ___ __ _ _ __ (_)_ __   __ _   / _|_ __ ___  _ __ ___    
|  _| / __|/ __/ _` | '_ \| | '_ \ / _` | | |_| '__/ _ \| '_ ` _ \   
| |___\__ \ (_| (_| | |_) | | | | | (_| | |  _| | | (_) | | | | | |  
|_____|___/\___\__,_| .__/|_|_| |_|\__, | |_| |_|  \___/|_| |_| |_|  
 _   _             _|_|          _ |___/              _          _ _ 
| |_| |__   ___   / _|_   _  ___| | _(_)_ __   __ _  | |__   ___| | |
| __| '_ \ / _ \ | |_| | | |/ __| |/ / | '_ \ / _` | | '_ \ / _ \ | |
| |_| | | |  __/ |  _| |_| | (__|   <| | | | | (_| | | | | |  __/ | |
 \__|_| |_|\___| |_|  \__,_|\___|_|\_\_|_| |_|\__, | |_| |_|\___|_|_|
                                              |___/                        made by xk4libur
""")

def option_1():
    print("\n1 - Sit quietly")
    print("2 - Walk until you find someone")
    print("3 - Find an exit")
    choice = input("\nChoose your option: ")
    return choice

def decision_1():
    choice = option_1()

    if choice == "1":
        print("\nYou decided to sit quietly waiting for something to happen, but nothing happens and you sit there for eternity. (You lost)\n")

    elif choice == "2":
        print("""\nAfter walking for a long time, you find some souls talking. 
You approach to ask where you are. One of the souls says that you are in the Ante-Hell, 
the only circle of Hell where there is no punishment.
You ask who these souls are, and they answer that they were unbaptized in life — among them is Socrates.
After a long conversation, you discover that you can get out of the Ante-Hell.\n""")

    elif choice == "3":
        print("\nYou decide to look for a way out on your own, but you don't discover any way out and you can't find anyone to go with you. (You lost)\n")

    else:
        print("\nSelect a valid option [1/3]\n")
        decision_1()  # vuelve a intentar

# Ejecutar la decisión
decision_1()

print("\nYou are a damned soul who has awakened in the depths of Hell and must escape by passing through different infernal circles, facing demons.\n")
time.sleep(3)
print("\nIn order to get out of hell, you have to get to the deepest point of hell, there is the main exit to the real world, but there is also Lucifer.\n")
time.sleep(3)
print("\nYour journey begins in the “ante-inferno” room, where you find all the damned souls who have died at the same time as you.\n")
time.sleep(3)
print("\nSuddenly, demons appear and begin to take all the souls to a pit where there is a demon in the form of a snake, the demon who judges the souls and takes them to different stages of hell.\n")
time.sleep(3)
print("\nWhen your turn comes, the demon stares you in the eyes and without saying anything, you become unconscious.\n")
time.sleep(3)
print("\nWhen you wake up, you discover that you are in a very quiet place, but you don't know what to do and you think of 3 different options:\n") # Option 1


