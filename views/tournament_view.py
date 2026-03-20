class TournamentView:
    def get_info(self):
        name = input("Nom du tournoi")
        starting_date = input("Date de début")
        ending_date = input("Date de fin")
        location = input("Lieu")
        number_of_rounds = input("Nombre de tours")
        return name, starting_date, ending_date, location, number_of_rounds

