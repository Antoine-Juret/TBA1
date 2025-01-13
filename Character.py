class Character():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.description = description
        self.msgs=msgs

    def __str__(self):
        """
        Retourne une représentation textuelle du personnage.

        :return: str, une chaîne décrivant le personnage
        """
        return f"{self.name} :{self.current_room}: {self.description}: {self.msgs}" 