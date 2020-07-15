import json
import os

path = "/home/eric/PycharmProjects/game_classes/"

games_list = []

class Boardgame:  # handles board games as objects with name, mix/max player, and estimated price
    # need to implement rating

    def __init__(self, name: str, player_mincount: int = 0, player_maxcount: int = 0, price: int = 0):
        self.name = name
        self.player_mincount = player_mincount
        self.player_maxcount = player_maxcount
        self.price = price

    def __repr__(self):
        return f"{self.name},{self.player_mincount},{self.player_maxcount},{self.price}"

    def __dict__(self):
        boardgame_dict = {
            'name': self.name,
            'player_mincount': self.player_mincount,
            'player_maxcount': self.player_maxcount,
            'price': self.price}
        return boardgame_dict

    @classmethod
    def get_from_json(cls):
        with open(f"{path}board_game_lib.json", 'r') as file:
            for game in json.load(file):
                games_list.append(game)
            return games_list

    def save_to_json(self):
        game_dict = self.__dict__()
        list_of_games = [game_dict]
        # print(games_list)
        with open(f"{path}board_game_lib.json", 'r+') as file:
            if os.stat(f"{path}board_game_lib.json").st_size != 0:
                for each in json.load(file):
                    list_of_games.append(each)
            # print(games_list)
            file.seek(0)
            json.dump(list_of_games, file, indent=2)
