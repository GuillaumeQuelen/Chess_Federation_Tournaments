from views.menu_view import MenuView
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController


class AppController:
    def __init__(self):
        self.menu = MenuView()
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController()

    def run(self):
        while True:
            choix = self.menu.show_menu()

            if choix == "1":
                self.player_controller.create_player()
            elif choix == "2":
                self.tournament_controller.run()
            elif choix == "4":
                print("Au revoir !")
                break