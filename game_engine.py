from helping_tools import *

class TossWinDecide:

    def __init__(self, player_choice_odd_or_even, player_choice_number, computer_choice_number): 
        self.player_toss_win = None
        self.player_choice_odd_or_even = player_choice_odd_or_even
        self.player_choice_number = player_choice_number
        self.computer_choice_number = computer_choice_number

    # Checks if player won the toss
    def checker(self):

        # Could use 'and' and 'or' statements, but thought to have it traditional instead of lengthy
        if (self.player_choice_number + self.computer_choice_number)%2 == 0:
            if(self.player_choice_odd_or_even == Choice.even): self.player_toss_win = Choice.win
            else: self.player_toss_win = Choice.lose
        else:
            if(self.player_choice_odd_or_even == Choice.odd): self.player_toss_win = Choice.win
            else: self.player_toss_win = Choice.lose
        
        return self.player_toss_win

# Inning implementation for both Player and Computer
class Inning:
    def __init__(self,Computer,Player,Helper,target=None):
        self.target = target
        self.Player = Player
        self.Helper = Helper
        self.Computer = Computer
        self.runs_scored = 0
        self.Number_of_balls = 0
        self.player_won = None

    def start_inning(self):
        temp_bat = 0
        temp_bowl = 0
        while True:
            print("*"*50)
            self.Number_of_balls += 1
            print(f"Ball Number: {self.Number_of_balls}")
            print(f"Runs: {self.runs_scored}")
            if self.Player.choice_bat_or_bowl == Choice.batting:
                temp_bat = self.Player.get_number()
                temp_bowl = self.Computer.get_number()
                print(f"You Chose: {temp_bat}")
                print(f"Computer Chose: {temp_bowl}")
                check = self.Helper.check_lost(temp_bat,temp_bowl,self.Player,self.Computer,self.runs_scored,self.target)

                if check == Choice.out:
                    print('*'*50)
                    print("Player OUT!")
                    print('*'*50)
                    self.Player.batting_runs = self.runs_scored
                    break
                elif check == Choice.lost:
                    print('*'*50)
                    print("Player LOST!")
                    print("Computer WON")
                    print('*'*50)
                    self.player_won = Choice.lost
                    self.Player.batting_runs = self.runs_scored
                    break
                elif check == Choice.draw:
                    print('*'*50)
                    print("DRAW!")
                    print('*'*50)
                    self.player_won = Choice.draw
                    self.Player.batting_runs = self.runs_scored
                    break

            elif self.Computer.choice_bat_or_bowl == Choice.batting:
                player_temp = self.Player.get_number()
                computer_temp = self.Computer.get_number()
                (temp_bowl,temp_bat) = self.Helper.is_cheating(player_temp,computer_temp)
                print(f"You Chose: {temp_bowl}")
                print(f"Computer Chose: {temp_bat}")
                check = self.Helper.check_lost(temp_bat,temp_bowl,self.Player,self.Computer,self.runs_scored,self.target)

                if check == Choice.out:
                    print('*'*50)
                    print("Computer OUT!")
                    print('*'*50)
                    self.Computer.batting_runs = self.runs_scored
                    break
                elif check == Choice.lost:
                    print('*'*50)
                    print("Player WON")
                    print("Computer LOST!")
                    print('*'*50)
                    self.player_won = Choice.won
                    self.Computer.batting_runs = self.runs_scored
                    break
                elif check == Choice.draw:
                    print('*'*50)
                    print("DRAW!")
                    print('*'*50)
                    self.player_won = Choice.draw
                    self.Computer.batting_runs = self.runs_scored
                    break
            
            # Intentional Rule (if batter keeps 0, the number of bowler transfers)
            if temp_bat == 0:
                self.runs_scored += temp_bowl
            else:
                self.runs_scored += temp_bat

            if self.Helper.check_win(temp_bat,temp_bowl,self.runs_scored,self.target) == Choice.won:
                if self.Computer.choice_bat_or_bowl == Choice.batting:
                    print('*'*50)
                    print("Computer WON!")
                    print('*'*50)
                    self.player_won = Choice.lost
                    self.Computer.batting_runs = self.runs_scored
                    break
                elif self.Player.choice_bat_or_bowl == Choice.batting:
                    print('*'*50)
                    print("Player WON!")
                    print('*'*50)
                    self.player_won = Choice.won
                    self.Player.batting_runs = self.runs_scored
                    break