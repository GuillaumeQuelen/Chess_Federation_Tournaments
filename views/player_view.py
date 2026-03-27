import re
from datetime import datetime


class PlayerView:
    def get_info(self):
        first_name = input("Prénom : ")
        last_name = input("Nom : ")

        while True:
            birth_date = input("Date de naissance (JJ/MM/AAAA) : ")
            try:
                date = datetime.strptime(birth_date, "%d/%m/%Y")
                if (datetime.now() - date).days > 150 * 365:
                    print("Âge invalide !")
                else:
                    break
            except ValueError:
                print("Date invalide ! Format : JJ/MM/AAAA")

        while True:
            national_id = input("Identifiant (ex: AB12345) : ").upper()
            if re.match(r"^[A-Z]{2}\d{5}$", national_id):
                break
            print("Format invalide ! Ex: AB12345")

        return first_name, last_name, birth_date, national_id
    def ask_continue(self):
        print("\nJoueur créé !")
        print("1. Ajouter un autre joueur")
        print("2. Retour au menu")
        return input("Votre choix : ")