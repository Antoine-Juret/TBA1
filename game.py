"""
Module game.py

Ce module contient la classe `Game` qui définit la logique principale d'un jeu d'aventure textuel. 
Le joueur interagit avec un environnement de pièces, objets, personnages et commandes.

Classes:
    Game: Gère la configuration, la boucle principale du jeu, et l'interaction utilisateur.

Fonctions:
    main(): Point d'entrée du jeu.

"""

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character


class Game:
    """
        Classe principale pour gérer le jeu d'aventure.

    Attributs:
        finished (bool): Indique si le jeu est terminé.
        rooms (list[Room]): Liste des pièces du jeu.
        commands (dict[str, Command]): Dictionnaire des commandes disponibles.
        player (Player): Le joueur qui participe au jeu.

    Méthodes:
        __init__(): Initialise une nouvelle instance de la classe Game.
        setup(): Configure les éléments du jeu (pièces, commandes, objets, personnages).
        play(): Démarre la boucle principale du jeu.
        check_victory_condition(): Vérifie si la condition de victoire est atteinte.
        process_command(command_string): Traite les commandes saisies par le joueur.
        print_welcome(): Affiche un message de bienvenue au joueur.
    """

    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None

    def setup(self):
        """
        Configure les éléments du jeu, y compris les pièces,
        les objets, les personnages et les commandes.

        Crée des pièces, des objets, des personnages non-joueurs (PNJ) et associe des sorties
        et des objets aux pièces. Configure également les commandes du joueur.
        """

        # création d'objets
        Fusil_lebel = Item(
            "Fusil_lebel", "fusil réglementaire de l'armée française", 4.5
        )
        grenade_f1 = Item("grenade_f1", "grenade a fragmentation", 0.5)
        casque_Adrian = Item("casque_Adrian", "Casque de l'armée française ", 0.750)
        Lettre_du_général = Item(
            "Lettre_du_général", "Ordre de repli signé par le général ", 0.2
        )

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command(
            "go",
            " <direction> : se déplacer dans une direction et haut en bas (N, E, S, O, U, D)",
            Actions.go,
            1,
        )
        self.commands["go"] = go
        history = Command(
            "history", " : affiche les pièces déjà visitées", Actions.get_history, 0
        )
        self.commands["history"] = history
        back = Command(
            "back",
            " : effectue un retour en arrière si cela est possible",
            Actions.get_back,
            0,
        )
        self.commands["back"] = back
        check = Command("check", " : afficher l'inventaire", Actions.check, 0)
        self.commands["check"] = check
        take = Command("take", " : permet de prendre un objet", Actions.take, 1)
        self.commands["take"] = take
        look = Command(
            "look",
            " : permet d'observer la pièce dans laquelle on se trouve",
            Actions.look,
            0,
        )
        self.commands["look"] = look
        drop = Command(
            "drop", " : permet de déposer un objet dans la pièce", Actions.drop, 1
        )
        self.commands["drop"] = drop
        talk = Command(
            "talk",
            " : permet d'échanger avec les personnages rencontrés",
            Actions.talk,
            1,
        )
        self.commands["talk"] = talk

        Quartier_général = Room("Quartier_général", "le Quartier Général Français.")
        self.rooms.append(Quartier_général)
        Caserne_Est = Room("Caserne_Est", "une Caserne située à l'Est du QG.")
        self.rooms.append(Caserne_Est)
        Caserne_Ouest = Room("Caserne_Ouest", "une Caserne située à l'Ouest du QG.")
        self.rooms.append(Caserne_Ouest)
        Cantine = Room("Cantine", "une Cantine dans laquelle mange des soldats.")
        self.rooms.append(Cantine)
        Armurerie = Room(
            "Armurerie", "une Armurerie, on peut y trouver des armes en tout genres."
        )
        self.rooms.append(Armurerie)
        Chemin_effondré = Room(
            "Chemin_effondré", "un chemin détruit à cause des bombardements allemands."
        )
        self.rooms.append(Chemin_effondré)
        Champs_de_mines = Room(
            "Champs_de_mines",
            "un grand champs, attention celui ci peut contenir des mines, ne bougez plus!",
        )
        self.rooms.append(Champs_de_mines)
        Moulin = Room(
            "Moulin", "un moulin qui n'est plus utilisé depuis le début de la guerre."
        )
        self.rooms.append(Moulin)
        Tour_d_observation = Room(
            "Tour_d_observation", "une tour d'observation très haute."
        )
        self.rooms.append(Tour_d_observation)
        Cave = Room(
            "Cave", "une cave très sombre, vous semblez y distinger un cadavre."
        )
        self.rooms.append(Cave)
        Toit = Room(
            "Toit", "le toit de la Tour, vous voyez l'ensemble du champs de bataille."
        )
        self.rooms.append(Toit)
        Char_abandonné = Room(
            "Char_abandonné",
            "un Sturmpanzerwagen A7V transpercé par un obus, il est encore fumant.",
        )
        self.rooms.append(Char_abandonné)
        Avant_poste_Allemand = Room(
            "Avant_poste_Allemand", " une pièce occupée par des allemands"
        )
        self.rooms.append(Avant_poste_Allemand)
        Tranchée_Nord = Room(
            "Tranchée_Nord",
            "une très grande tranchée située au nord de la zone des combats.",
        )
        self.rooms.append(Tranchée_Nord)
        Position_Avancée = Room(
            "Position_Avancée",
            "une position avancée, là où se situe le Commandant Raynal.",
        )
        self.rooms.append(Position_Avancée)

        # création des pnj
        soldat_allemand = Character(
            "soldat_allemand",
            Avant_poste_Allemand,
            "un soldat allemand monte la garde",
            [" Halte ou j'ouvre le feu !!", " Fire !! "],
        )
        Commandant_Raynal = Character(
            "Commandant_Raynal",
            Position_Avancée,
            "Le Commandant Raynal qui va lancer l'assault",
            ["Dépèchez vous on va attaquer", "Avez vous une lettre ?"],
        )

        Quartier_général.exits = {
            "N": Armurerie,
            "E": Caserne_Est,
            "S": None,
            "O": Caserne_Ouest,
            "U": None,
            "D": None,
        }
        Caserne_Est.exits = {
            "N": None,
            "E": None,
            "S": None,
            "O": Quartier_général,
            "U": None,
            "D": None,
        }
        Caserne_Ouest.exits = {
            "N": None,
            "E": Quartier_général,
            "S": None,
            "O": Cantine,
            "U": None,
            "D": None,
        }
        Cantine.exits = {
            "N": None,
            "E": Caserne_Ouest,
            "S": None,
            "O": None,
            "U": None,
            "D": None,
        }
        Armurerie.exits = {
            "N": Chemin_effondré,
            "E": Moulin,
            "S": Quartier_général,
            "O": Champs_de_mines,
            "U": None,
            "D": None,
        }
        Champs_de_mines.exits = {
            "N": None,
            "E": None,
            "S": None,
            "O": None,
            "U": None,
            "D": None,
        }
        Chemin_effondré.exits = {
            "N": None,
            "E": None,
            "S": Armurerie,
            "O": None,
            "U": None,
            "D": None,
        }
        Moulin.exits = {
            "N": Avant_poste_Allemand,
            "E": Tour_d_observation,
            "S": None,
            "O": Armurerie,
            "U": None,
            "D": None,
        }
        Tour_d_observation.exits = {
            "N": Char_abandonné,
            "E": None,
            "S": None,
            "O": Avant_poste_Allemand,
            "U": Toit,
            "D": Cave,
        }
        Cave.exits = {
            "N": None,
            "E": None,
            "S": None,
            "O": None,
            "U": Tour_d_observation,
            "D": None,
        }
        Toit.exits = {
            "N": None,
            "E": None,
            "S": None,
            "O": None,
            "U": None,
            "D": Tour_d_observation,
        }
        Char_abandonné.exits = {
            "N": Tranchée_Nord,
            "E": None,
            "S": Tour_d_observation,
            "O": Avant_poste_Allemand,
            "U": None,
            "D": None,
        }
        Avant_poste_Allemand.exits = {
            "N": Tranchée_Nord,
            "E": Char_abandonné,
            "S": Moulin,
            "O": None,
            "U": None,
            "D": None,
        }
        Tranchée_Nord.exits = {
            "N": None,
            "E": None,
            "S": Char_abandonné,
            "O": Position_Avancée,
            "U": None,
            "D": None,
        }
        Position_Avancée.exits = {
            "N": None,
            "E": Tranchée_Nord,
            "S": None,
            "O": None,
            "U": None,
            "D": None,
        }

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = Quartier_général

        # assignation des objets au lieux
        Quartier_général.inventory.add(Lettre_du_général)
        Caserne_Est.inventory.add(grenade_f1)
        Caserne_Est.inventory.add(Fusil_lebel)
        Caserne_Est.inventory.add(casque_Adrian)
        # Assignation des pnj aux lieux
        Avant_poste_Allemand.Character.add(soldat_allemand)
        Position_Avancée.Character.add(Commandant_Raynal)

    def play(self):
        """
        Démarre la boucle principale du jeu. Le jeu continue jusqu'à ce que l'objectif soit atteint
        ou que le joueur quitte.
        """
        self.setup()
        self.print_welcome()
        while not self.finished:
            self.process_command(input("> "))

            # Vérifier si le joueur a atteint l'objectif de fin
            if self.check_victory_condition():
                print("\nCommandant_Raynal dit" " : " "Il n'y aura pas d'attaque finalement.")
                print("\nFélicitations, vous avez gagné le jeu!")
                self.finished = True  # Mettre fin au jeu
            if self.check_victory_condition():
                print("\nLe jeu est terminé.")

            if self.check_failed_condition():
                print("\nVous etes tombé dans un champ de mines, vous avez perdu!")
                self.finished = True  # Mettre fin au jeu
            if self.check_victory_condition():
                print("\nRecommencer!.")

        return None

    def check_victory_condition(self):
        """
        Vérifie si la condition de victoire est atteinte.

        Returns:
            bool: True si la condition est atteinte, False sinon.
        """
        # Exemple de condition de fin : le joueur doit atteindre une certaine pièce

        if self.player.current_room.name == "Position_Avancée":
            for i in self.player.current_room.inventory:
                if i.name == "Lettre_du_général":
                    return True  # Le joueur a gagné
        return False

    def check_failed_condition(self):
        """
        Vérifie si la condition d'échec est atteinte.

        Returns:
            bool: True si la condition est atteinte, False sinon.
        """
        # Exemple de condition de fin : le joueur doit atteindre une certaine pièce

        if self.player.current_room.name == "Champs_de_mines":
            return True


    def process_command(self, command_string) -> None:
        """
        Traite une commande saisie par le joueur.

        Args:
            command_string (str): La commande saisie par le joueur.
        """


        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]
        if command_string == "":
            return

        if command_word not in self.commands.keys():
            print(
                f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n"
            )


        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)


    def print_welcome(self):
        """
        Affiche un message de bienvenue au joueur.
        """
        print(
            f"\nBienvenue {self.player.name} dans notre jeu d'aventure !\n\nVous avez pour mission de délivrer la lettre du général au commandant Raynal."
        )
        print("\n" "Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())


def main():
    """
    Point d'entrée pour lancer le jeu.
    """
    Game().play()


if __name__ == "__main__":
    main()
