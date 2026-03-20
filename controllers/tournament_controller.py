from views.tournament_view import TournamentView
from models.tournament import Tournament

class TournamentController:
    def __init__(self):
        self.view = TournamentView()
        self.tournament = []
    
    def create_tournament(self):
        #Récupérer l'information
        name, starting_date, ending_date, location, number_of_rounds = self.view.get_info()

        #Créer le tournoi
        tournament = Tournament(name, starting_date, ending_date, location, number_of_rounds)

        #Ajouter aux données
        self.tournament.append(tournament)
        
        return tournament

