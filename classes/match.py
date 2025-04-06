class Match:
    def __init__(self, teams, result):
        self.teams = teams  # Lista con 2 objetos Team
        self.result = result  # Ejemplo: "2-1"

    def display_result(self):
        print(f"{self.teams[0].name} vs {self.teams[1].name} --> Resultado: {self.result}")
