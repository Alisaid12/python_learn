from classes.person import Person

class Coach(Person):
    def __init__(self, fname, lname, age, tactic):
        super().__init__(fname, lname, age)
        self.tactic = tactic

    def display_info(self):
        print(f"Coach: {self.fname} {self.lname} | Edad: {self.age} | Táctica: {self.tactic}")
