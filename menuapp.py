from typing import List

from boardgames import Boardgame

#wingspan = boardgames.Boardgame("Wingspan", 1, 6, 80)
#wingspan.save_to_json()
#scythe = boardgames.Boardgame("Scythe", 1, 6, 100)
#scythe.save_to_json()
# for games in Boardgame.get_from_json():
#     print (games['name'])

menu = """
    ---Please select an option---
    1 - add games to list
    2 - view list
    0 - EXIT AND SAVE
    999 - Exit WITHOUT saving changes
"""


def add_to_working_list(new_games_list):
    add_game_name = "start"
    while add_game_name != "":
        add_game_name = input("Please give the name of the game to be added: (leave blank to return to menu) ")
        if add_game_name != "":
            add_game_mincount = input("The minimum number of players: ")
            add_game_maxcount = input("The maximum number of players: ")
            add_game_price = int(input("Value of the game in USD (enter 0 if unsure): "))
            new_games_list.append(Boardgame(add_game_name, add_game_mincount, add_game_maxcount, add_game_price))


def display_game(game: dict):
    print(f"{game.name} allows for {game.player_mincount} to {game.player_maxcount} players, estimated "
          f"cost: ${game.price}")


def view_list(existing_games_list: List, new_games_list: List):
    print("Games already in library: ")
    game: Boardgame
    for game in existing_games_list:
        display_game(game)
    for game in new_games_list:
        display_game(game)


def save_list_objects(new_games_list: List):
    for each in new_games_list:
        each.save_to_json()


def load_list(existing_games_list: List):
    for game in Boardgame.get_from_json():
        existing_games_list.append(Boardgame(game['name'], game['player_mincount'], game['player_maxcount'], game['price']))


def main_menu():
    new_games_list = []
    existing_games_list =[]
    load_list(existing_games_list)
    selection = ""
    while selection != "999" and selection != "0":
        selection = input(menu)
        if selection == "1":
            add_to_working_list(new_games_list)
        elif selection == "2":
            view_list(existing_games_list, new_games_list)
        elif selection == "0":
            save_list_objects(new_games_list)

main_menu()