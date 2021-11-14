class Tournoi:
    def __init__(self, nom, lieu, date_tournoi, rounds, players,
                 controle_temps, description,
                 nombre_de_tours=4):
        self.nom = nom
        self.lieu = lieu
        self.date_tournoi = date_tournoi
        self.nombre_de_tours = nombre_de_tours
        self.rounds = rounds
        """liste des instances ronds"""
        self.players = players
        """Liste des indices correspondant aux instances joueurstockéesenmémoire"""
        self.controle_temps: controle_temps
        """C'est toujours un bullet, un blitz ou un coup rapide"""
        self.description: description

