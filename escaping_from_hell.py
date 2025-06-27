#!/usr/bin/env/python3

import time
import sys

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
    return input("\nChoose your option: ")

def decision_1():
    choice = option_1()
    if choice == "1":
        print("\nYou sit and wait for eternity. (You lost)\n")
        sys.exit()
    elif choice == "2":
        print("""\nYou find souls talking. They tell you you're in the Ante-Hell.
Among them is Socrates. They help you move on.\n""")
    elif choice == "3":
        print("\nYou find nothing and perish in solitude. (You lost)\n")
        sys.exit()
    else:
        print("\nSelect a valid option [1/3]\n")
        decision_1()

def option_2():
    print("\n1 - Search for the most recognized souls")
    print("2 - Go straight to the golden tornado")
    print("3 - Avoid tornadoes and keep your feet on the ground")
    return input("\nChoose your option: ")

def decision_2():
    choice = option_2()
    if choice == "1":
        print("\nYou're swept away by the winds. (You lost)\n")
        sys.exit()
    elif choice == "2":
        print("\nYou rise through the golden tornado and reach the next circle.\n")
    elif choice == "3":
        print("\nYou get caught by a storm. (You lost)\n")
        sys.exit()
    else:
        print("\nSelect a valid option [1/3]\n")
        decision_2()

def decision_3():
    print("\nYou arrive in a place where rain never stops and the ground is mud.\n")
    print("\n1 - Eat from the ground with other souls")
    print("2 - Shout at the rain demanding mercy")
    print("3 - Hide in a ruined structure")
    choice = input("\nChoose your option: ")
    if choice == "1":
        print("\nYou are trapped in gluttony forever. (You lost)\n")
        sys.exit()
    elif choice == "2":
        print("\nA demon hears your cries and devours you. (You lost)\n")
        sys.exit()
    elif choice == "3":
        print("\nYou find a hidden passage to the next circle.\n")
    else:
        print("\nSelect a valid option [1/3]\n")
        decision_3()

def decision_4():
    print("\nYou find two groups eternally crashing into each other.\n")
    print("1 - Join the group shouting about greed")
    print("2 - Walk alone among them, looking for a pattern")
    print("3 - Sit down and meditate")
    choice = input("\nChoose your option: ")
    if choice == "1":
        print("\nYou are crushed in the eternal cycle of greed. (You lost)\n")
        sys.exit()
    elif choice == "2":
        print("\nYou notice a hidden path and sneak through to the next circle.\n")
    elif choice == "3":
        print("\nA soul drags you into its obsession. (You lost)\n")
        sys.exit()
    else:
        print("\nSelect a valid option [1/3]\n")
        decision_4()

def decision_5():
    print("\nYou reach a river of wrath where souls fight endlessly in the water.\n")
    print("1 - Jump into the river and fight")
    print("2 - Try to speak with a calm soul underwater")
    print("3 - Wait for a boat to arrive")
    choice = input("\nChoose your option: ")
    if choice == "1":
        print("\nYou drown in eternal rage. (You lost)\n")
        sys.exit()
    elif choice == "2":
        print("\nThe calm soul shows you a hidden tunnel. You escape to the next circle.\n")
    elif choice == "3":
        print("\nThe boat never comes. (You lost)\n")
        sys.exit()
    else:
        print("\nSelect a valid option [1/3]\n")
        decision_5()

def decision_6():
    print("\nYou find burning tombs where heretics are punished.\n")
    print("1 - Enter a tomb seeking answers")
    print("2 - Search the area for keys or artifacts")
    print("3 - Run across the tombs without stopping")
    choice = input("\nChoose your option: ")
    if choice == "1":
        print("\nYou are locked inside forever. (You lost)\n")
        sys.exit()
    elif choice == "2":
        print("\nYou find a cracked tomb with a passage to the next circle.\n")
    elif choice == "3":
        print("\nYou fall into a pit of fire. (You lost)\n")
        sys.exit()
    else:
        print("\nSelect a valid option [1/3]\n")
        decision_6()

def decision_7():
    print("\nIn this circle, violence reigns. Rivers of boiling blood surround you.\n")
    print("1 - Swim across the boiling river")
    print("2 - Ask the centaurs guarding it for help")
    print("3 - Use a fallen tree to cross")
    choice = input("\nChoose your option: ")
    if choice == "1":
        print("\nYou boil alive. (You lost)\n")
        sys.exit()
    elif choice == "2":
        print("\nA centaur shows you the path for the brave. You pass.\n")
    elif choice == "3":
        print("\nThe tree sinks and you fall in. (You lost)\n")
        sys.exit()
    else:
        print("\nSelect a valid option [1/3]\n")
        decision_7()

def decision_8():
    print("\nYou arrive in a place filled with liars, seducers, and thieves.\n")
    print("1 - Bargain with a demon")
    print("2 - Pretend to be one of the sinners")
    print("3 - Stay silent and observe")
    choice = input("\nChoose your option: ")
    if choice == "1":
        print("\nThe demon deceives and destroys you. (You lost)\n")
        sys.exit()
    elif choice == "2":
        print("\nYou are mistaken for a real sinner and tortured. (You lost)\n")
        sys.exit()
    elif choice == "3":
        print("\nYou see a pattern in the illusions and sneak past to the final circle.\n")
    else:
        print("\nSelect a valid option [1/3]\n")
        decision_8()

def decision_9():
    print("\nAt last, you arrive at the frozen lake of traitors, where Lucifer is imprisoned.\n")
    print("1 - Try to speak to Lucifer")
    print("2 - Climb Lucifer’s back while he's frozen")
    print("3 - Look for a crack in the ice to escape")
    choice = input("\nChoose your option: ")
    if choice == "1":
        print("\nLucifer wakes and devours your soul. (You lost)\n")
        sys.exit()
    elif choice == "2":
        print("\nYou climb carefully and find a hidden passage leading out of Hell.\n")
        print("\nCONGRATULATIONS. YOU HAVE ESCAPED HELL.\n")
        sys.exit()
    elif choice == "3":
        print("\nYou fall into the icy abyss. (You lost)\n")
        sys.exit()
    else:
        print("\nSelect a valid option [1/3]\n")
        decision_9()

# INICIO DEL JUEGO
print("\nYou are a damned soul who has awakened in the depths of Hell and must escape by passing through different infernal circles.\n")
time.sleep(3)

decision_1()
time.sleep(3)
decision_2()
time.sleep(3)
decision_3()
time.sleep(3)
decision_4()
time.sleep(3)
decision_5()
time.sleep(3)
decision_6()
time.sleep(3)
decision_7()
time.sleep(3)
decision_8()
time.sleep(3)
decision_9()