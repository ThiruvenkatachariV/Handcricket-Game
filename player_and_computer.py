from helping_tools import *
from random import randint

class PlayerInputs:

    def __init__(self):
        self.batting_runs = 0
        self.choice_odd_or_even = None
        self.choice_number = None
        self.choice_bat_or_bowl = None

    # Gets the player choice mapped to Odd or Even
    # Odd -> 1 ; Even -> 2
    def get_odd_or_even(self):
        while True:
            temp = input("Enter Odd (O) or Even (E): ").lower()
            if(temp in ['odd','o','1']):
                self.choice_odd_or_even = Choice.odd
                break
            elif(temp in ['eve','even','2','0','e']):
                self.choice_odd_or_even = Choice.even
                break
            else:
                print("Enter a Valid Choice!")
        return self.choice_odd_or_even
    
    # Gets the player number choice for toss
    def get_number(self):
        while True:
            temp = input("Enter a Number from (0-10): ")
            if temp in map(lambda x:str(x),list(range(0,11))):
                self.choice_number = int(temp)
                break
            else:
                print("Enter a Valid Choice!")
        return self.choice_number
    
    # Player Choice for Batting or Bowling first
    def get_bat_or_bowl(self):
        while True:
            temp = input("Enter Batting (1) or Bowling (0): ").lower()
            if(temp in ['1','batting','bat']):
                self.choice_bat_or_bowl = Choice.batting
                break
            elif(temp in ['0','bowling','bowl']):
                self.choice_bat_or_bowl = Choice.bowling
                break
        return self.choice_bat_or_bowl
        
class ComputerInputs:

    def __init__(self):
        self.choice_number = None
        self.batting_runs = 0
        self.choice_bat_or_bowl = None

    # Gets the computer number choice for toss
    def get_number(self):
        self.choice_number = randint(0,10)
        return self.choice_number
    
    # Gets choice if computer bowling or batting first
    def get_computer_bat_or_bowl(self):
        self.choice_bat_or_bowl = randint(0,1)
        return self.choice_bat_or_bowl