from views.player_view import PlayerView
from models.player import Player
import os
import json


class PlayerController:
    def __init__(self):
        self.view = PlayerView()
        self.players = []

    def create_player(self):
        first_name, last_name, birth_date, national_id = self.view.get_info()
        player = Player(last_name, first_name, birth_date, national_id)
        self.players.append(player)
        self.save_players()    # ← manquait cette ligne !
        return player

    def save_players(self):
        os.makedirs("data", exist_ok=True)
        with open("data/players.json", "w") as f:
            json.dump([p.to_dict() for p in self.players], f, indent=4)