import pyautogui, time, os, colorama
from colorama import Fore

os.system("title SpamBot by TheAndrei#5771")
os.system("cls")

print(f'''{Fore.LIGHTBLUE_EX}
                                      _____                       ____        _   
                                     / ____|                     |  _ \      | |  
                                    | (___  _ __   __ _ _ __ ___ | |_) | ___ | |_ 
                                     \___ \| '_ \ / _` | '_ ` _ \|  _ < / _ \| __|
                                     ____) | |_) | (_| | | | | | | |_) | (_) | |_ 
                                    |_____/| .__/ \__,_|_| |_| |_|____/ \___/ \__|
                                           | |                                    
                                           |_|
''')                                    
print(f'''{Fore.YELLOW}This is a very simple spam bot coded by TheAndrei.
Instructions: Just type the message you want to spam, how many times you want the message to be spammed and how much \ntime between each message in secconds (ex. 0, 0.1, 3, etc.), then hit enter and press the input box where you want to \nspam, the spam will begin in 5 seconds.
''')
print(f'''{Fore.LIGHTRED_EX}NOTE: THIS TOOL CAN CAUSE CHAOS IF NOT USED IN THE RIGHT WAY. IN SIMPLE WORDS IT WILL WRITE THE MESSAGE AND PRESS \nENTER OVER AND OVER AGAIN SO BE CAREFULL WHAT WINDOW AND INPUT BOX YOUR COMPUTER IS FOCUSED ON
''')
print(f"{Fore.LIGHTBLUE_EX}You can contact me on discord: TheAndrei#0001 \n ")

msg = input(f"{Fore.GREEN}Message to spam: ")
times = input(f"{Fore.GREEN}\nHow many times: ")
cldwn = input(f"{Fore.GREEN}\nHow much time between each message: ")
print(f"{Fore.GREEN}\nThe spamm will begin in :")

count = 5
while count != 0:
	print(count)
	time.sleep(1)
	count -= 1

os.system("cls")
print(f"{Fore.GREEN}Spamming...")

for i in range(0,int(times)):
       pyautogui.typewrite(msg + '\n')
       time.sleep(float(cldwn))

os.system("cls")

print(f"{Fore.GREEN}Spam complete. This window will close in 10 secconds")
time.sleep(1)
os.system("cls")
print(f"{Fore.GREEN}Spam complete. This window will close in 9 secconds")
time.sleep(1)
os.system("cls")
print(f"{Fore.GREEN}Spam complete. This window will close in 8 secconds")
time.sleep(1)
os.system("cls")
print(f"{Fore.GREEN}Spam complete. This window will close in 7 secconds")
time.sleep(1)
os.system("cls")
print(f"{Fore.GREEN}Spam complete. This window will close in 6 secconds")
time.sleep(1)
os.system("cls")
print(f"{Fore.GREEN}Spam complete. This window will close in 5 secconds")
time.sleep(1)
os.system("cls")
print(f"{Fore.GREEN}Spam complete. This window will close in 4 secconds")
time.sleep(1)
os.system("cls")
print(f"{Fore.GREEN}Spam complete. This window will close in 3 secconds")
time.sleep(1)
os.system("cls")
print(f"{Fore.GREEN}Spam complete. This window will close in 2 secconds")
time.sleep(1)
os.system("cls")
print(f"{Fore.GREEN}Spam complete. This window will close in 1 secconds")
time.sleep(1)
