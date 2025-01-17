"""
La classe item gère les objets du jeu,
ont peut y retrouver de plusieurs informations comme son nom, 
sa description et sa masse.
"""
class Item:
    """
     Classe représentant l'objet.

    Attributs:
    ----------
    name : str
        Le nom de l'objet.
    description : str
        Description détaillé de l'objet.
    weight: str
        La masse de l'objet
    """
    def __init__(self, name, description, weight):
        """
        Initialise un objet avec un nom, une description et un poids.

         name: str, le nom de l'objet
         description: str, la description de l'objet
         weight: int ou float, le poids de l'objet en kilogrammes
        """
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        """
        Retourne une représentation textuelle de l'objet.

        :return: str, une chaîne décrivant l'objet
        """
        return f"{self.name} : {self.description} ({self.weight} kg)"
