
"""
La classe Player gère les informations relatives au joueur, comme son nom, 
la pièce où il se trouve actuellement, l'historique des pièces visitées, 
et son inventaire.
"""
class Player():
    """
    Classe représentant le joueur.

    Attributs:
    ----------
    name : str
        Le nom du joueur.
    current_room : Room | None
        La pièce où se trouve actuellement le joueur.
    history : list[Room]
        L'historique des pièces visitées.
    inventory : dict[str, Item]
        L'inventaire du joueur, où les clés sont les noms des objets et les 
        valeurs sont des instances d'Item.
    """


    def __init__(self, name):
        """
        initialise un joueur avec un nom, un historique vide, et un inventaire vide.

        Paramètres:
        -----------
        name : str
            Le nom du joueur.
        """
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = {}  # Liste des objets ramassés


    def move(self, direction):
        """
        Tente de déplacer le joueur dans une direction donnée.

        Paramètres:
        -----------
        direction : str
        La direction dans laquelle le joueur souhaite se déplacer.

        Retourne:
        ---------
        bool
        True si le déplacement est réussi, False sinon.
        """
        next_room = self.current_room.exits[direction]

        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        self.history.append(self.current_room)

        self.current_room = next_room
        print(self.current_room.get_long_description())
        #Pièces déjà vivsité
        print("\nVous avez déjà visité les pièces suivantes:")
        for i in (self.history):
            print( "\t","-",i.name)
        return True

    def get_inventory(self):
        """
          Affiche les objets actuellement dans l'inventaire du joueur.

        Si l'inventaire est vide, affiche un message indiquant que l'inventaire
        ne contient aucun objet.
        """
        if not self.inventory:
            print("\nVotre inventaire est vide.\n")
        else:
            print("\nInventaire :")
            for j in self.inventory:
                print("\t","-",j)
