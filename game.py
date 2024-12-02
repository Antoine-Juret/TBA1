# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale et de haut en bas (N, E, S, O, U, D)", Actions.go, 1)
        self.commands["go"] = go
        
        # Setup rooms

        Quartier_général = Room("Quartier_général", "le Quartier Général Français.")
        self.rooms.append(Quartier_général)
        Caserne_Est= Room("Caserne_Est", "une Caserne située à l'Est du QG.")
        self.rooms.append(Caserne_Est)
        Caserne_Ouest = Room("Caserne_Ouest", "une Caserne située à l'Ouest du QG.")
        self.rooms.append(Caserne_Ouest)
        Cantine = Room("Cantine", "une Cantine dans laquelle mange des soldats.")
        self.rooms.append(Cantine)
        Armurerie = Room("Armurerie", "une Armurerie, on peut y trouver des armes en tout genres.")
        self.rooms.append(Armurerie)
        Chemin_effondré = Room("Chemin_effondré", "un chemin détruit à cause des bombardements allemands.")
        self.rooms.append(Chemin_effondré)
        Champs_de_mines = Room("Champs_de_mines", "un grand champs, attention celui ci peut contenir des mines, ne bougez plus!")
        self.rooms.append(Champs_de_mines)
        Moulin = Room("Moulin", "un moulin qui n'est plus utilisé depuis le début de la guerre.")
        self.rooms.append(Moulin)
        Tour_d_observation = Room("Tour_d_observation", "une tour d'observation très haute.")
        self.rooms.append(Tour_d_observation)
        Cave = Room("Cave", "une cave très sombre, vous semblez y distinger un cadavre.")
        self.rooms.append(Cave)
        Toit= Room("Toit", "le toit de la Tour, vous voyez l'ensemble du champs de bataille.")
        self.rooms.append(Toit)
        Char_abandonné = Room("Char_abandonné", "un Sturmpanzerwagen A7V transpercé par un obus, il est encore fumant.")
        self.rooms.append(Char_abandonné)
        Avant_poste_Allemand = Room("Avant_poste_Allemand", " une pièce occupée par des allemands")
        self.rooms.append(Avant_poste_Allemand)
        Tranchée_Nord = Room("Tranchée_Nord", "une très grande tranchée située au nord de la zone des combats.")
        self.rooms.append(Tranchée_Nord)
        Position_Avancée = Room("Position_Avancée", "une position avancée, là où se situe le Commandant Raynel.")
        self.rooms.append(Position_Avancée)





        # Create exits for rooms

        Quartier_général.exits = {"N" : Armurerie, "E" : Caserne_Est, "S" : None, "O" : Caserne_Ouest, "U" : None, "D" : None}
        Caserne_Est.exits = {"N" : None, "E" : None, "S" : None, "O" : Quartier_général, "U" : None, "D" : None}
        Caserne_Ouest.exits = {"N" : None, "E" : Quartier_général, "S" : None, "O" : Cantine, "U" : None, "D" : None}
        Cantine.exits = {"N" : None, "E" : Caserne_Ouest, "S" : None, "O" : None, "U" : None, "D" : None}
        Armurerie.exits = {"N" : Chemin_effondré, "E" : Moulin, "S" : Quartier_général, "O" : Champs_de_mines, "U" : None, "D" : None}
        Champs_de_mines.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : None, "D" : None}
        Chemin_effondré.exits = {"N" : None, "E" : None, "S" : Armurerie, "O" : None, "U" : None, "D" : None}
        Moulin.exits = {"N" : Avant_poste_Allemand, "E" : Tour_d_observation, "S" : None, "O" : Armurerie, "U" : None, "D" : None}
        Tour_d_observation.exits = {"N" : Char_abandonné, "E" : None, "S" : None, "O" : Avant_poste_Allemand, "U" : Toit, "D" : Cave}
        Cave.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : Tour_d_observation, "D" : None}
        Toit.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : None, "D" : Tour_d_observation}
        Char_abandonné.exits = {"N" : Tranchée_Nord, "E" : None, "S" : Tour_d_observation, "O" : Avant_poste_Allemand, "U" : None, "D" : None}
        Avant_poste_Allemand.exits = {"N" : Tranchée_Nord, "E" : Char_abandonné, "S" : Moulin, "O" : None, "U" : None, "D" : None}
        Tranchée_Nord.exits = {"N" : None, "E" : None, "S" : Char_abandonné, "O" : Position_Avancée, "U" : None, "D" : None}
        Position_Avancée.exits = {"N" : None, "E" : Tranchée_Nord, "S" : None, "O" : None, "U" : None, "D" : None}

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = Quartier_général

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:


        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]
        if command_string == "":
            return
        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
