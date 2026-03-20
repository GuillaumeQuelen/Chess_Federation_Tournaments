from views.player_view import PlayerView
from models.player import Player


class PlayerController:
    def __init__(self):
        self.view = PlayerView()
        self.players = []
    
    def create-player(self):
        #Récupérer l'information
        first_name, last_name, birth_date, national_id = self.view.get_info()

        #Créer le joueur
        player = Player(last_name, first_name, birth_date, national_id)

        #Ajouter aux données
        self.players.append(player)

        return player

        