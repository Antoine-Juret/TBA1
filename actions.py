# Description: The actions module.
from player import Player
from room import Room

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:

    def go(game, list_of_words, number_of_parameters):
    
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction or up or down(N, E, S, O, U, D).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        dictDirections = {
        "N": ["N", "n", "Nord", "nord","NORD"],
        "S": ["S", "s", "sud","Sud","SUD"],
        "E": ["E", "e", "Est", "est","EST"],
        "O": ["Ouest", "ouest", "o", "O","OUEST"],
        "U": ["U","u","up","Up","UP"],
        "D": ["D","d","down","Down","DOWN"]
        }
        
        
        player = game.player
        l = len(list_of_words)
        
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
       #Interface amélioré     
        userInput = list_of_words[1]
        
        for key, val in dictDirections.items():
            for v in val:
                if(userInput == v):
                    player.move(key)
                    return True

        print("La direction '", userInput, "' n'est pas reconnue")
        return False
        #interface amélioré

        # Get the direction from the list of words.
        #direction = list_of_words[1].upper()
        # Move the player in the direction specified by the parameter.
        #player.move(direction)
        #return True

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

    def get_history(game, list_of_words, number_of_parameters):
        player = game.player
        if player.history:
            print("\nPièces déjà visitées :")
            for i in player.history:
                print("-",i.name)
        return True
    
    def get_back(game,list_of_words, number_of_parameters):
        player = game.player
        if (len(player.history) != 0):
                # Set the current room to the next room.
            player.next_room = player.history[len(player.history) -1]
            player.current_room = player.next_room
            player.history.pop()
            print(player.current_room.get_long_description())
            #Pièces déjà vivsité
            if len(player.history) > 0:
                print("\nVous avez déjà visité les pièces suivantes:")
                for i in (player.history):
                    print("-",i.name)
                return True
            else :
                print("Vous n'avez pas visité d'autre pièce.")
                return True
        print(player.current_room.get_long_description())
        return True

    def check(game, list_of_words, number_of_parameters):
        """
        Affiche l'inventaire du joueur.

        Args:
            game (Game): L'objet du jeu.
            list_of_words (list): Les mots de la commande.
            number_of_parameters (int): Le nombre de paramètres attendus.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.
        """
        # Vérification du nombre de paramètres
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Appel de la méthode get_inventory sur le joueur
        game.player.get_inventory()
        return True
    
    def look(game,list_of_words, number_of_parameters):
       if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
       player = game.player
       Room.get_inventory(player.current_room)
       return True
    
    def take (game,list_of_words, number_of_parameters):
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        player = game.player
        iteme = list_of_words[1]
        for item in player.current_room.inventory:
            if iteme==item.name:
                player.inventory[item.name]=item
                player.current_room.inventory.remove(item)
                return True



    def drop (game,list_of_words, number_of_parameters):
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        player=game.player
        iteme = list_of_words[1]
        if iteme in player.inventory.keys():
            del player.inventory[iteme]
            (player.current_room).inventory.add(iteme)
            return True