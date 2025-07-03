class Choice:
    odd = 1
    even = 2
    win = 1
    lose = 0
    batting = 1
    bowling = 0
    
    out = 4
    lost = 5
    won = 6
    draw = 7

class Helper:

    def __init__(self,Player,Computer):
        self.Player = Player
        self.Computer = Computer
        self.cheat_checker = []

    def resetBowl(self,bowl,bat):
        while bowl == bat:
            bat = self.Computer.get_number()
        return (bowl,bat)

    def is_cheating(self,bowl,bat):
        if len(self.cheat_checker) == 0:
            self.cheat_checker.append(bowl)
            return (bowl,bat)
        elif len(self.cheat_checker) == 1:
            if bowl in self.cheat_checker:
                self.cheat_checker.append(bowl)
            else:
                self.cheat_checker = []
            return (bowl,bat)
        elif len(self.cheat_checker) == 2:
            if bowl in self.cheat_checker:
                print("Spam Detected! Anti-Cheat Activated!")
                return self.resetBowl(bowl,bat)
            else:
                self.cheat_checker = []
                return (bowl,bat)
            
    def check_lost(self,temp_bat,temp_bowl,Player,Computer,current_runs,target=None):
        if temp_bat == temp_bowl:
            if Player.choice_bat_or_bowl == Choice.batting:
                if target == None:
                    return Choice.out
                else:
                    if target > current_runs:
                        return Choice.lost
                    else:
                        return Choice.draw
                    
            else:
                if target == None:
                    return Choice.out
                else:
                    if target > current_runs:
                        return Choice.lost
                    else:
                        return Choice.draw

    def check_win(self,temp_bat,temp_bowl,current_runs,target):
        if temp_bat != temp_bowl and target != None:
            if current_runs > target:
                    return Choice.won
        
    def result(self, Innings_2):
        if Innings_2.player_won == Choice.won:
            return "Player WON"
        elif Innings_2.player_won == Choice.lost:
            return "Player LOST"
        elif Innings_2.player_won == Choice.draw:
            return "DRAW"
