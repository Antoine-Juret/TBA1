# Define the Room class.
"""
Module contenant la classe Room, qui représente une pièce 
dans notre jeu.
Chaque pièce possède un nom, une description, des sorties,
un inventaire d'objets et des personnages.
"""

class Room:
    """
      Classe représentant une pièce dans un jeu.

    Attributs:
        name (str): Le nom de la pièce.
        description (str): La description de la pièce.
        exits (dict): Un dictionnaire où les clés sont les directions (str) et les valeurs
                      sont les pièces associées.
        inventory (set): Un ensemble représentant les objets présents dans la pièce.
        characters (dict): Un dictionnaire où les clés sont les noms des personnages (str)
                           et les valeurs leurs descriptions (str).

    """

    # Define the constructor.
    def __init__(self, name, description):
        """
        Initialise une nouvelle instance de la classe Room.

        Args:
            name (str): Le nom de la pièce.
            description (str): La description de la pièce.
        """
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = set()
        self.Character = set()

    # Define the get_exit method.
    def get_exit(self, direction):
        """
        Récupère la pièce dans une direction donnée.

        Args:
            direction (str): La direction pour laquelle récupérer la pièce.

        Returns:
            Room or None: La pièce dans la direction spécifiée, ou None si elle n'existe pas.
        """

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]

    # Return a string describing the room's exits.
    def get_exit_string(self):
        """
         Renvoie une chaîne décrivant les sorties disponibles depuis cette pièce.

        Returns:
            str: Une chaîne listant les directions accessibles.
        """
        exit_string = "Sorties: "
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        """
        Renvoie une description détaillée de la pièce, incluant son nom,
        sa description et les sorties.
        Returns:
            str: La description complète de la pièce.
        """
        return f"\nVous êtes dans {self.name} {self.description}\n\n{self.get_exit_string()}\n"

    def get_inventory(self):
        """
        Affiche le contenu de l'inventaire de la pièce et les personnages présents.

        Returns:
            bool: True après avoir affiché le contenu de la pièce.
        """
        if not self.inventory:
            print("Il n'y a pas d'objet dans la pièce.")
        else:
            for elt in self.inventory:
                print("\t","-",elt)
        if not self.Character:
            print("Il n'y a personne dans la pièce.")
        else:
            print("Il y a :")
            for elt in self.Character:
                print("\t","-", elt.name ,":", elt.description)
        return True
