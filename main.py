import json
from classes.player import Player
from classes.coach import Coach
from classes.team import Team
from classes.match import Match


DATA_FILE = 'data/data.json'

def load_data():
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"teams": [], "matches": []}

    teams = []
    team_lookup = {}

    for team_data in data.get("teams", []):
        coach_data = team_data.get("coach")
        coach = Coach(coach_data["fname"], coach_data["lname"], coach_data["age"], coach_data["tactic"])
        team = Team(team_data["name"], coach, team_data.get("stadium"))

        for player_data in team_data.get("player", []):
            player = Player(player_data["fname"], player_data["lname"], player_data["age"], team.name, player_data["score_goal"])
            team.add_player(player)

        teams.append(team)
        team_lookup[team.name] = team  # Para reconstruir los partidos después

    # Reconstruir partidos
    from classes.match import Match
    matches = []
    for match_data in data.get("matches", []):
        team1 = team_lookup.get(match_data["teams"][0])
        team2 = team_lookup.get(match_data["teams"][1])
        if team1 and team2:
            match = Match([team1, team2], match_data["result"])
            matches.append(match)

    return teams, matches



def teams_to_dict(teams):
    """
    Convierte la lista de objetos Team en un diccionario con la estructura para JSON.
    """
    data = {"teams": []}
    for team in teams:
        team_dict = {
            "name": team.name,
            "coach": {
                "fname": team.coach.fname,
                "lname": team.coach.lname,
                "age": team.coach.age,
                "tactic": team.coach.tactic
            },
            "player": [],
            "stadium": team.stadium
        }
        for player in team.players:
            team_dict["player"].append({
                "fname": player.fname,
                "lname": player.lname,
                "age": player.age,
                "team": player.team,
                "score_goal": player.score_goal
            })
        data["teams"].append(team_dict)
    return data

def save_data(teams, matches):
    data = teams_to_dict(teams)
    data["matches"] = []

    for match in matches:
        data["matches"].append({
            "teams": [match.teams[0].name, match.teams[1].name],
            "result": match.result
        })

    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)
    print("Datos guardados correctamente.")


# Menú para gestionar equipos (agregar, elegir, eliminar, mostrar)
def team_management_menu(teams,matches):
    while True:
        print("\n=== Menú de Gestión de Equipos ===")
        print("1. Agregar equipo")
        print("2. Seleccionar equipo")
        print("3. Eliminar equipo")
        print("4. Mostrar equipos")
        print("5. Crear partido")
        print("6. Mostrar partidos")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            add_team(teams)
            save_data(teams)
        elif opcion == "2":
            team = select_team(teams)
            if team:
                main_team_menu(team)
                save_data(teams)
        elif opcion == "3":
            remove_team(teams)
            save_data(teams)
        elif opcion == "4":
            display_teams(teams)
        elif opcion == "5":
            create_match(teams, matches)
            save_data(teams, matches)
        elif opcion == "6":
            display_matches(matches)
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

def add_team(teams):
    print("\n--- Agregar Equipo ---")
    team_name = input("Nombre del equipo: ")
    
    print("Ingrese los datos del coach:")
    coach_fname = input("Nombre: ")
    coach_lname = input("Apellido: ")
    try:
        coach_age = int(input("Edad: "))
    except ValueError:
        print("La edad debe ser un número entero.")
        return
    tactic = input("Táctica: ")
    coach = Coach(coach_fname, coach_lname, coach_age, tactic)
    
    stadium = input("Nombre del estadio: ")
    
    new_team = Team(team_name, coach, stadium)
    teams.append(new_team)
    print(f"Equipo '{team_name}' agregado exitosamente.")

def select_team(teams):
    if not teams:
        print("No hay equipos disponibles.")
        return None
    print("\n--- Seleccionar Equipo ---")
    for idx, team in enumerate(teams):
        print(f"{idx}. {team.name}")
    try:
        index = int(input("Ingrese el índice del equipo a seleccionar: "))
    except ValueError:
        print("Índice inválido.")
        return None
    if 0 <= index < len(teams):
        return teams[index]
    else:
        print("Índice no válido.")
        return None

def remove_team(teams):
    if not teams:
        print("No hay equipos para eliminar.")
        return
    print("\n--- Eliminar Equipo ---")
    for idx, team in enumerate(teams):
        print(f"{idx}. {team.name}")
    try:
        index = int(input("Ingrese el índice del equipo a eliminar: "))
    except ValueError:
        print("Índice inválido.")
        return
    if 0 <= index < len(teams):
        removed_team = teams.pop(index)
        print(f"Equipo '{removed_team.name}' eliminado exitosamente.")
    else:
        print("Índice no válido.")

def display_teams(teams):
    if not teams:
        print("No hay equipos registrados.")
        return
    print("\n--- Equipos Registrados ---")
    for team in teams:
        print(f"Equipo: {team.name}")
        print(" Coach:")
        print(f"  {team.coach.fname} {team.coach.lname}, Edad: {team.coach.age}, Táctica: {team.coach.tactic}")
        print(" Estadio:", team.stadium)
        print(" Jugadores:")
        if team.players:
            for player in team.players:
                print(f"  {player.fname} {player.lname}")
        else:
            print("  No hay jugadores")
        print("-" * 30)


def create_match(teams, matches):
    if len(teams) < 2:
        print("Se necesitan al menos dos equipos para jugar un partido.")
        return

    print("\n--- Crear Partido ---")
    for idx, team in enumerate(teams):
        print(f"{idx}. {team.name}")
    
    try:
        idx1 = int(input("Seleccione el índice del primer equipo: "))
        idx2 = int(input("Seleccione el índice del segundo equipo: "))
        if idx1 == idx2:
            print("Un equipo no puede jugar contra sí mismo.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    if 0 <= idx1 < len(teams) and 0 <= idx2 < len(teams):
        result = input("Resultado del partido (ej. 3-1): ")
        match = Match([teams[idx1], teams[idx2]], result)
        matches.append(match)
        print("\n--- Resultado del Partido ---")
        match.display_result()
    else:
        print("Índices de equipos no válidos.")

def display_matches(matches):
    if not matches:
        print("No hay partidos registrados.")
        return

    print("\n--- Partidos Registrados ---")
    for match in matches:
        match.display_result()



# Menú para gestionar un equipo seleccionado (jugadores, coach, estadio)
def main_team_menu(team):
    while True:
        print(f"\n=== Gestión del Equipo: {team.name} ===")
        print("1. Agregar jugador")
        print("2. Eliminar jugador")
        print("3. Mostrar jugadores")
        print("4. Cambiar coach")
        print("5. Agregar/Actualizar estadio")
        print("6. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- Agregar Jugador ---")
            fname = input("Nombre: ")
            lname = input("Apellido: ")
            try:
                age = int(input("Edad: "))
                score_goal = int(input("Cantidad de goles: "))
            except ValueError:
                print("Edad y goles deben ser números enteros.")
                continue
            new_player = Player(fname, lname, age, team.name, score_goal)
            team.add_player(new_player)
        elif opcion == "2":
            print("\n--- Eliminar Jugador ---")
            if not team.players:
                print("No hay jugadores para eliminar.")
            else:
                for idx, player in enumerate(team.players):
                    print(f"{idx}. {player.fname} {player.lname}")
                try:
                    index = int(input("Ingrese el índice del jugador a eliminar: "))
                except ValueError:
                    print("Índice inválido.")
                    continue
                if 0 <= index < len(team.players):
                    team.remove_player(team.players[index])
                else:
                    print("Índice no válido.")
        elif opcion == "3":
            print("\n--- Mostrar Jugadores ---")
            team.display_players()
        elif opcion == "4":
            print("\n--- Cambiar Coach ---")
            fname = input("Nombre del nuevo coach: ")
            lname = input("Apellido del nuevo coach: ")
            try:
                age = int(input("Edad: "))
            except ValueError:
                print("La edad debe ser un número entero.")
                continue
            tactic = input("Táctica: ")
            new_coach = Coach(fname, lname, age, tactic)
            team.change_coach(new_coach)
        elif opcion == "5":
            print("\n--- Agregar/Actualizar Estadio ---")
            stadium = input("Nombre del estadio: ")
            team.add_stadium(stadium)
        elif opcion == "6":
            break
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    teams, matches = load_data()
    team_management_menu(teams, matches)
    save_data(teams, matches)
