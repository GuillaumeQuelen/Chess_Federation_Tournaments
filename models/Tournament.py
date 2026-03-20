class Tournament:
    def __init__(self, name, starting_date, ending_date, current_round, number_of_rounds, players_list, description, location, rounds):
        self.name = name
        self.starting_date = starting_date
        self.ending_date = ending_date
        self.current_round = 0
        self.number_of_rounds = 4
        self.players_list = players_list
        self.description = description
        self.location = location
        self.rounds = []