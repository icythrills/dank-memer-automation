import sys
from colorama import Back
from random import randint
from colorama.ansi import Fore
import pyautogui as p
import time

def beg():
    p.typewrite('pls beg', interval=0.05)
    p.press('enter')


def fish():
    p.typewrite('pls fish', interval=0.05)
    p.press('enter')

# def hunt():
#     p.typewrite('pls hunt', interval=0.05)
#     p.press('enter')

def deposit():
    p.typewrite('pls deposit all', interval=0.05)
    p.press('enter')


def search():
    p.typewrite('pls search', interval=0.05)
    p.press('enter')
    time.sleep(5)
    p.typewrite('air')
    p.press('enter')

counter = 0
while True:
    try:
        rand = randint(40, 50)
        print(
            Back.LIGHTBLUE_EX,
            'Sleeping  ',
            Back.RESET,
            f'{rand} {Fore.MAGENTA}s{Fore.RESET}',
        )
        time.sleep(rand)
        print(
            Back.LIGHTRED_EX,
            'Begging   ',
            Back.RESET,
        )
        beg()
        # print(
        #     Back.CYAN,
        #     'Hunting   ',
        #     Back.RESET,
        # )
        # hunt()
        # time.sleep(2)
        print(
            Back.BLUE,
            'Fishing   ',
            Back.RESET,
        )
        fish()
        time.sleep(2)
        print(
            Back.LIGHTBLUE_EX,
            'Searching ',
            Back.RESET
        )
        search()
        print(
            Back.GREEN,
            'Depositing',
            Back.RESET
        )
        deposit()
        counter += 1

        print(
            Back.LIGHTMAGENTA_EX,
            'Iteration ', 
            Back.RESET,
            counter,
        )

    except KeyboardInterrupt:
        print(f'{Fore.LIGHTRED_EX}Terminated.{Fore.RESET}')
        sys.exit()