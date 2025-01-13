# Define the Room class.

class Room:

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = set()
        self.Character = {}
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes dans {self.name} {self.description}\n\n{self.get_exit_string()}\n"
    
    def get_inventory(self):
        if not self.inventory:
            print("Il n'y a pas d'objet dans la pièce.")
        else:
            for elt in self.inventory:
                print("\t","-",elt)
        if not self.Character:
            print("Il n'y a personne dans la pièce.")
        else:
            print("Il y a :")
            for key in self.Character:
                print("\t","-", key)
        return True
        
