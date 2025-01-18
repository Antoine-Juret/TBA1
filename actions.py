"""
Module Actions

Ce module contient toutes les actions qui peuvent être exécutées 
lorsqu'une commande est donnée dans le jeu.
Chaque action est représentée par une méthode statique dans la classe `Actions`. 
Ces méthodes permettent d'exécuter 
des commandes spécifiques et de gérer les interactions du joueur avec le jeu.

Classes:
    - Actions: Classe contenant les méthodes statiques pour exécuter les commandes du jeu.
"""
from room import Room

MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:
    """
      La classe Actions

    Cette classe regroupe l'ensemble des actions que le joueur peut exécuter dans le jeu. 
    Chaque action correspond à une méthode statique de la classe et représente une commande 
    pouvant être donnée par le joueur, comme se déplacer, quitter le jeu, afficher l'inventaire, 
    ou interagir avec l'environnement.

    Méthodes principales :
        - go : Permet de déplacer le joueur dans une direction donnée.
        - quit : Termine le jeu en affichant un message d'adieu.
        - help : Affiche la liste des commandes disponibles.
        - get_history : Affiche l'historique des pièces visitées par le joueur.
        - get_back : Retourne à la pièce précédente visitée.
        - check : Affiche l'inventaire du joueur.
        - look : Montre les objets présents dans la pièce actuelle.
        - take : Permet au joueur de ramasser un objet dans la pièce actuelle.
        - drop : Permet au joueur de déposer un objet dans la pièce actuelle.
        - talk : Engage un dialogue avec un personnage présent dans la pièce.

    Utilisation :
    Les méthodes de cette classe sont statiques et 
    sont appelées directement avec le préfixe `Actions.`
    Elles prennent en paramètres les objets nécessaires 
    pour exécuter la commande (comme l'état du jeu 
    ou les mots de la commande) et renvoient un booléen indiquant 
    si l'action a été exécutée avec succès.
    """
    @staticmethod
    def go(game, list_of_words, number_of_parameters):

        """
           Déplace le joueur dans la direction spécifiée.

    La direction doit être une des suivantes : N, E, S, O, U, D ou leurs variantes 
    (Nord, Est, Sud, Ouest, Up, Down).

    Args:
        game (Game): L'objet du jeu.
        list_of_words (list): Liste des mots de la commande.
        number_of_parameters (int): Nombre attendu de paramètres.

    Returns:
        bool: True si la commande a été exécutée avec succès, False sinon.

    Examples:
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> Actions.go(game, ["go", "N"], 1)
        True
        >>> Actions.go(game, ["go", "X"], 1)
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
    @staticmethod
    def quit(game, list_of_words, number_of_parameters):
        """
        Quitte le jeu en affichant un message d'adieu.

    Args:
        game (Game): L'objet du jeu.
        list_of_words (list): Liste des mots de la commande.
        number_of_parameters (int): Nombre attendu de paramètres.

    Returns:
        bool: True si la commande a été exécutée avec succès, False sinon.

        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True
    @staticmethod
    def help(game, list_of_words, number_of_parameters):
        """
          Affiche la liste des commandes disponibles dans le jeu.

    Args:
        game (Game): L'objet du jeu.
        list_of_words (list): Liste des mots de la commande.
        number_of_parameters (int): Nombre attendu de paramètres.

    Returns:
        bool: True si la commande a été exécutée avec succès, False sinon.
        """

        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Affiche les commandes
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True
    @staticmethod
    def get_history(game, list_of_words, number_of_parameters):
        """
        Affiche l'historique des pièces visitées par le joueur.

    Args:
        game (Game): L'objet du jeu.
        list_of_words (list): Liste des mots de la commande.
        number_of_parameters (int): Nombre attendu de paramètres.

    Returns:
        bool: True.
        """
        player = game.player
        if player.history:
            print("\nPièces déjà visitées :")
            for i in player.history:
                print("\t","-", i.name , i.description)
        return True
    @staticmethod
    def get_back(game,list_of_words, number_of_parameters):
        """
            Ramène le joueur à la pièce précédente dans l'historique.

    Args:
        game (Game): L'objet du jeu.
        list_of_words (list): Liste des mots de la commande.
        number_of_parameters (int): Nombre attendu de paramètres.

    Returns:
        bool: True si le joueur peut revenir en arrière, False sinon.
        """
        player = game.player
        if (len(player.history) != 0):
            player.next_room = player.history[len(player.history) -1]
            player.current_room = player.next_room
            player.history.pop()
            print(player.current_room.get_long_description())
            #Pièces déjà vivsité
            if len(player.history) > 0:
                print("\nVous avez déjà visité les pièces suivantes:")
                for i in (player.history):
                    print("\t","-",i.name,",",i.description)
                return True
            else :
                print("Vous n'avez pas visité d'autre pièce.")
                return True
        print(player.current_room.get_long_description())
        return True
    @staticmethod
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
    @staticmethod
    def look(game,list_of_words, number_of_parameters):
        """
            Affiche les objets disponibles dans la pièce actuelle.

        Args:
        game (Game): L'objet du jeu.
        list_of_words (list): Liste des mots de la commande.
        number_of_parameters (int): Nombre attendu de paramètres.

        Returns:
        bool: True si la commande a été exécutée avec succès, False sinon.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        player = game.player
        Room.get_inventory(player.current_room)
        return True
    @staticmethod
    def take (game,list_of_words, number_of_parameters):
        """
          Permet au joueur de ramasser un objet dans la pièce actuelle.

    Args:
        game (Game): L'objet du jeu.
        list_of_words (list): Liste des mots de la commande.
        number_of_parameters (int): Nombre attendu de paramètres.

    Returns:
        bool: True si l'objet a été ramassé avec succès, False sinon.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        player = game.player
        iteme = list_of_words[1]
        for item in player.current_room.inventory:
            if iteme==item.name:
                player.inventory[item]=item    #player.inventory[item.name]=item
                player.current_room.inventory.remove(item)
                return True
        else :
            print("L\' objet n\'existe pas")


    @staticmethod
    def drop (game,list_of_words, number_of_parameters):
        """
         Permet au joueur de déposer un objet dans la pièce actuelle.

    Args:
        game (Game): L'objet du jeu.
        list_of_words (list): Liste des mots de la commande.
        number_of_parameters (int): Nombre attendu de paramètres.

    Returns:
        bool: True si l'objet a été déposé avec succès, False sinon.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        player=game.player
        iteme = list_of_words[1]
        for ite in player.inventory:
            #print(ite)
            if iteme==ite.name:
                #print(ite)
                del player.inventory[ite]#del player.inventory[iteme]
                (player.current_room).inventory.add(ite) #(player.current_room).inventory.add(iteme)
            return True
        else :
            print("L\' objet n\'existe pas")
        return True
    @staticmethod
    def talk (game,list_of_words, number_of_parameters):
        """
            Permet au joueur de parler avec un personnage présent dans la pièce actuelle.

    Args:
        game (Game): L'objet du jeu.
        list_of_words (list): Liste des mots de la commande.
        number_of_parameters (int): Nombre attendu de paramètres.

    Returns:
        bool: True si un dialogue a eu lieu avec succès, False sinon.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        player = game.player
        nom = list_of_words[1]


        for j in player.current_room.Character:
            if j.name == nom:
                j.get_msg()  # Appel de la méthode get_msg sur l'instance du personnage
            return True

        print(f"\t{nom} ne parle pas.")
        return True
