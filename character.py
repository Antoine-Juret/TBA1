class Character():

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
        for i in room.Character:
            print(i.msgs)
        return True