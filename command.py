"""
Ce module contient la classe `Command`, qui représente une commande. 
Chaque commande est définie par un mot-clé, un texte d'aide, une action à exécuter, 
et le nombre de paramètres requis.

Classes:
    Command: Représente une commande et fournit les informations 
    nécessaires pour son exécution.


"""

class Command:
    """
    Représente une commande dans le jeu. Une commande est composée d'un mot-clé, d'un texte d'aide, 
    d'une action à exécuter et du nombre de paramètres requis.

    Attributes:
        command_word (str): Le mot-clé de la commande.
        help_string (str): La description ou l'aide associée à la commande.
        action (fonction): La fonction à exécuter lorsque la commande est appelée.
        number_of_parameters (int): Le nombre de paramètres attendus par la commande.

    Methods:
        __init__(self, command_word, help_string, action, number_of_parameters):
            Initialise une nouvelle instance de la commande.
        __str__(self):
            Retourne une représentation textuelle de la commande.
    """

    # The constructor.
    def __init__(self, command_word, help_string, action, number_of_parameters):
        self.command_word = command_word
        self.help_string = help_string
        self.action = action
        self.number_of_parameters = number_of_parameters

    # The string representation of the command.
    def __str__(self):
        return  self.command_word \
                + self.help_string
