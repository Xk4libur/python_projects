#!/usr/bin/env/python3


print(r""" 
 ____  _                      _  _         
|  _ \| |__   ___  _ __   ___| || |  _   _ 
| |_) | '_ \ / _ \| '_ \ / _ \ || |_| | | |
|  __/| | | | (_) | | | |  __/__   _| |_| |
|_|   |_| |_|\___/|_| |_|\___|  |_|  \__,_|
                                                made by xk4libur
""")

option = input("\nWhich OS do you want [I] iOS or [A] Android? -->  ")

if option == "I":
    option_2 = input("\nDo you have a large budget for an iPhone? [Y/N] -->  ")
    if option_2 == "Y":
        print("\n[+] Buy the latest iPhone model.\n")
    elif option_2 == "N":
        print("\n[+] Buy a second-hand iPhone or an iPhone released in previous years.\n")
    else:
        print("\nPlease select a valid option [Y/N].\n")

elif option == "A":
    option_3 = input("\nDo you have a large budget for an Android device? [Y/N] -->  ")
    if option_3 == "Y":
        option_4 = input("\nDo you mind the camera? [Y/N] -->  ")
        if option_4 == "Y":
            print("\n[+] Buy a Google Pixel.\n")
        elif option_4 == "N":
            option_5 = input("\nDo you prefer a gaming phone? [Y/N] -->  ")
            if option_5 == "Y":
                print("\n[+] Buy a gaming phone: ROG, Red Magic, or Black Shark.\n")
            elif option_5 == "N":
                print("\n[+] Buy a high-end Android: Samsung, OnePlus, Xiaomi, or Realme.\n")
            else:
                print("\nPlease select a valid option [Y/N].\n")
        else:
            print("\nPlease select a valid option [Y/N].")
    elif option_3 == "N":
        print("\n[+] Look for mid-range Android phones like Galaxy A series, Redmi Note, or Poco.\n")
    else:
        print("\nPlease select a valid option [Y/N].\n")

else:
    print("\nInvalid option. Please choose [I] for iOS or [A] for Android.\n")