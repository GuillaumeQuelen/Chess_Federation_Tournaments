from views.menu_view import MenuView
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController

class AppController:
    def __init__(self):
        self.view = MenuView()
        self.view = PlayerController()
        self.view = TournamentController()

     def run(self):
    while True:
        choix = self.menu.show_menu()
        
        if choix == "1":
            self.player_controller.create_player()
        elif choix == "2":
            self.tournament_controller.create_tournament()
        elif choix == "4":
            print("Au revoir !")
            break