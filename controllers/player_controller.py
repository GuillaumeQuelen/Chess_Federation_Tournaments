
from models import player
from models.player import Player
from views.player_view import PlayerView
from data_manager import save_players, load_players

class PlayerController:
    def __init__(self):
        self.view = PlayerView()
        self.players = []

    def create_player(self):
        first_name, last_name, birth_date, national_id = self.view.get_info()
        player = Player(last_name, first_name, birth_date, national_id)
        self.players.append(player)
        save_players(self.players)    # ← 1. on sauvegarde
        choix = self.view.ask_continue()  # ← 2. on demande
        if choix == "1":
            self.create_player()
        return player

