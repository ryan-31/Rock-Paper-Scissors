# -------------------------------------------
# Created by Ryan S (GitHub: ryan-31)
# 9/27/21
# Version 1.0
# Basic console based rock paper scissors.
# Future plans are to add a GUI
# -------------------------------------------

import random


def convert_to_value(text: str) -> int:
    if text.upper() == "ROCK":
        return 1
    elif text.upper() == "PAPER":
        return 2
    else:
        return 3


def rev_convert(num: int) -> str:
    if num == 1:
        return "Rock"
    elif num == 2:
        return "Paper"
    else:
        return "Scissors"


def cpu_turn() -> int:
    return random.randrange(1, 3)


def game(user: int, cpu: int, player_str: str) -> str:
    if user == cpu:
        return "\aIt's a tie!\nYour choice: " + player_str + "\nCPU's choice: " + rev_convert(cpu)
    elif user == 1 and cpu == 2:
        # rock vs paper
        return "\aYou Lost!\nYour choice: " + player_str + "\nCPU's choice: " + rev_convert(cpu)
    elif user == 1 and cpu == 3:
        # rock vs scissors
        return "\aYou Wom!\nYour choice: " + player_str + "\nCPU's choice: " + rev_convert(cpu)
    elif user == 2 and cpu == 1:
        # paper vs rock
        return "\aYou Won!\nYour choice: " + player_str + "\nCPU's choice: " + rev_convert(cpu)
    elif user == 2 and cpu == 3:
        # paper vs scissors
        return "\aYou Lost!\nYour choice: " + player_str + "\nCPU's choice: " + rev_convert(cpu)
    elif user == 3 and cpu == 1:
        # scissors vs rock
        return "\aYou Lost!\nYour choice: " + player_str + "\nCPU's choice: " + rev_convert(cpu)
    else:
        # scissors vs paper
        return "\aYou Won!\nYour choice: " + player_str + "\nCPU's choice: " + rev_convert(cpu)


print("Welcome to Rock Paper Scissors - Type rock, paper, or scissors on 'scissors!'")
print("Ready?\nRock...")
print("Paper...")
playerInput = input("Scissors!")
player = convert_to_value(playerInput)
cpuVal = cpu_turn()
print(game(player, cpuVal, playerInput))
