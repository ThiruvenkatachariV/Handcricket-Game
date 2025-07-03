from os import path
from datetime import datetime
from player_and_computer import *
from game_engine import *

def main():
    while True:
        print()
        print("------------------------ HANDCRICKET GAME ------------------------")
        Player = PlayerInputs()
        Computer = ComputerInputs()
        Help = Helper(Player,Computer)

        player_choice = Player.get_odd_or_even()
        print(f"You Chose: {"Odd" if player_choice == Choice.odd else "Even"}")
        print(f"Computer Chose: {"Even" if player_choice == Choice.odd else "Odd"}")
        print('*'*50)

        player_choice_num = Player.get_number()
        computer_choice_num = Computer.get_number()
        print(f"You Chose: {player_choice_num}")
        print(f"Computer Chose: {computer_choice_num}")

        Ampire = TossWinDecide(player_choice,player_choice_num,computer_choice_num)
        player_win_toss = Ampire.checker()

        # Check for choosing and assign for first Innings
        if(player_win_toss):
            print(f"Player Won the toss!")
            if Player.get_bat_or_bowl() == Choice.batting:
                print("Player Chose to Bat")
                print("Computer has to Bowl")
                Computer.choice_bat_or_bowl = Choice.bowling
            else:
                print("Player Chose to Bowl")
                print("Computer has to Bat")
                Computer.choice_bat_or_bowl = Choice.batting
        else:
            print(f"Computer Won the toss!")
            if Computer.get_computer_bat_or_bowl() == Choice.batting:
                print("Computer Chose to Bat")
                print("Player has to Bowl")
                Player.choice_bat_or_bowl = Choice.bowling
            else:
                print("Computer Chose to Bowl")
                print("Player has to Bat")
                Player.choice_bat_or_bowl = Choice.batting

        print("*"*50)
        Innings_1 = Inning(Computer, Player,Help)
        print("First Innings Start!")
        Innings_1.start_inning()

        print(f"Number of Balls Played: {Innings_1.Number_of_balls}")
        print(f"Number of Runs Scored: {Innings_1.runs_scored}")
        print(f"Number of Runs Required to Win: {Innings_1.runs_scored + 1}")
        Computer.choice_bat_or_bowl = Choice.batting if Computer.choice_bat_or_bowl == Choice.bowling else Choice.bowling
        Player.choice_bat_or_bowl = Choice.batting if Player.choice_bat_or_bowl == Choice.bowling else Choice.bowling


        Innings_2 = Inning(Computer,Player,Help,Innings_1.runs_scored)
        Innings_2.start_inning()

        game_save(Player,Computer,Innings_1,Innings_2,Help)
        print('*'*50)
        if input("Press:\n\tTo Play Again: Press Enter\n\tTo Exit: Type E\n").lower() in ['e','exit','quit']: 
            print('*'*50)
            print("Thank You For Playing!")
            print('*'*50)
            break


def game_save(Player,Computer,Innings_1,Innings_2,Help):
    temp = input("Enter Name for Saving your Game: ").upper()
    try:
        fname = f"{temp}_{datetime.now().strftime('%Y_%m_%d___%H_%M_%S')}.txt"
        fpath = path.join("GameScores", fname)
        with open(fpath,'w') as f:
            f.write(f"""
    MATCH HISTORY OF {temp}
    RESULT: {Help.result(Innings_2)}
    FIRST INNINGS:
        PLAYER: {"Batting" if Player.choice_bat_or_bowl == Choice.bowling else "Bowling"}
        COMPUTER: {"Batting" if Computer.choice_bat_or_bowl == Choice.bowling else "Bowling"}
        NUMBER OF BALLS PLAYED: {Innings_1.Number_of_balls}
        RUNS SCORED IN FIRST INNINGS: {Innings_1.runs_scored}
    SECOND INNINGS:
        PLAYER: {"Batting" if Player.choice_bat_or_bowl == Choice.batting else "Bowling"}
        COMPUTER: {"Batting" if Computer.choice_bat_or_bowl == Choice.batting else "Bowling"}
        NUMBER OF BALLS PLAYED: {Innings_2.Number_of_balls}
        RUNS SCORED IN SECOND INNINGS: {Innings_2.runs_scored}
    """)
        print("Game saved Successfully!")
        print("Check the Path ./GameScores/")
    except Exception as e:
        print(e)
        print("Unexpected Error to Save the Game!")

main()