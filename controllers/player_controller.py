from player_view import PlayerView

class PlayerController:
    def create_player(self):
        self.view =Player.view()
        self.players = []
    
    def create-player(self):
        #Récupérer l'information
        first_name, last_name, birth_date, national_id = self.view.get_info()

        #Créer le joueur
        player = Player(last_name, first_name, birth_date, national_id)

        #Ajouter aux données
        self.players.append(player)
        
        return player

        