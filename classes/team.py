class Team:
    def __init__(self, name, coach, stadium=None):
        self.name = name
        self.players = []  # Lista para almacenar objetos Player
        self.coach = coach  # Objeto Coach
        self.stadium = stadium  # Puede ser None o una cadena con el nombre del estadio

    def add_player(self, player):
        self.players.append(player)
        print(f"Jugador {player.fname} {player.lname} agregado al equipo {self.name}.")

    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)
            print(f"Jugador {player.fname} {player.lname} eliminado del equipo {self.name}.")
        else:
            print("El jugador no se encuentra en el equipo.")

    def change_player(self, old_player, new_player):
        if old_player in self.players:
            index = self.players.index(old_player)
            self.players[index] = new_player
            print(f"Jugador {old_player.fname} ha sido reemplazado por {new_player.fname}.")
        else:
            print("El jugador a reemplazar no se encuentra en el equipo.")

    def display_players(self):
        if self.players:
            print(f"Jugadores del equipo {self.name}:")
            for player in self.players:
                player.display_info()
        else:
            print("No hay jugadores en el equipo.")

    def change_coach(self, new_coach):
        self.coach = new_coach
        print(f"Nuevo coach asignado: {new_coach.fname} {new_coach.lname}.")

    def add_stadium(self, stadium):
        self.stadium = stadium
        print(f"El estadio del equipo {self.name} es ahora {self.stadium}.")
