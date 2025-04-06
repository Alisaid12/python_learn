from classes.person import Person

class Player(Person):
    def __init__(self, fname, lname, age, team, score_goal):
        super().__init__(fname, lname, age)
        self.team = team
        self.score_goal = score_goal

    def display_info(self):
        print(f"Jugador: {self.fname} {self.lname} | Edad: {self.age} | Goles: {self.score_goal}")
