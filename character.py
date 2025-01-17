"""
Module character.py

Ce module contient la classe `Character`, qui représente un personnage .
Un personnage est associé à une pièce (room), possède un nom, une description,
 et des messages (msgs) qui peuvent être affichés ou utilisés pour interagir.

Classes:
    Character: Représente un personnage avec ses attributs et comportements.

Classes Importées:
    Room (depuis room.py): Pour gérer les interactions avec les pièces.
    Player (depuis player.py): Représente le joueur dans le jeu.
"""

from room import Room
from player import Player

class Character():
    """
        Classe représentant un personnage dans le jeu.

    Attributs:
        name (str): Le nom du personnage.
        current_room (Room | None): La pièce où se trouve le personnage actuellement.
        description (str): Une description du personnage.
        msgs (list[str]): Une liste de messages associés au personnage.
    """

    # Define the constructor.
    def __init__(self, name, current_room, description, msgs):
        self.name = name
        self.current_room = None
        self.description = description
        self.msgs = msgs

    def __str__(self):
        """
        Retourne une représentation textuelle du personnage.

        :return: str, une chaîne décrivant le personnage
        """
        return f"{self.name} :{self.current_room}: {self.description}: {self.msgs}"

    def get_msg(self):
        """
            Affiche les messages du personnage et interagit avec les messages associés aux pièces.

        Returns:
            bool: True si les messages ont été affichés correctement.
        """
        if self.msgs:
            # Prendre le premier message et l'afficher
            msg = self.msgs.pop(0)
            print("oui")
            print(msg)
            print(f"{self.name} dit : {msg}")
            # Ajouter ce message à la fin de la liste pour le rendre disponible pour le prochain appel
            self.msgs.append(msg)

        #Room.get_msg(self)
        return True
