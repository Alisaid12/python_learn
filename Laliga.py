class Person():
    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age

class Player(Person):
    def __init__(self, fname, lname, age,team,score_goal):
        super().__init__(fname, lname, age)    
        self.team = team 
        self.score_goal = score_goal 
        
    def display_info(self):
        print(f'The info of player is {self.fname} {self.lname}, Age: {self.age}, Team: {self.team}, Goals: {self.score_goal}')


class Coach(Person):
    def __init__(self, fname, lname, age,team,tactic):
        super().__init__(fname, lname, age)
        self.team = team 
        self.tactic = tactic 
    def display_info(self):
        print(f'The info of couch is {self.fname} {self.lname}, Age: {self.age}, Team: {self.team}, Tactic: {self.tactic}')

    
        
class Team():
    def __init__(self,name,player,coach,stadium):
        self.name = name
        self.player = player
        self.coach = coach
        self.stadium = stadium
    def add_player(self):
        pass
    def remove_player(self):
        pass
    def change_player(self):
        pass
    def display_players(self):
        pass
    def change_couch():
        pass 

class Match():
    def __init__(self,teams: list,result):
        self.teams = teams
        self.result = result
    def display_result(self):
        pass
        