class PlayerView:
    def get_info(self):
        first_name = input("Prénom: ")
        last_name = input("Nom: ")
        birth_date = input("Date de naissance: ")
        national_id = input("Identifiant: ")
        return first_name, last_name, birth_date, national_id
    
    def display_players(self, players):
        for player in players:
            print(player.first_name, player.last_name, player.national_id)
        