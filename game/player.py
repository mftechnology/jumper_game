class Player:
    """ A person who insert letter to the game. 

    Attributes:
        
        self.letterinput (String) with the letter input

    """

    def __init__(self,letter):
        """Constructs a new Hider.

        Args:
            self (Hider): An instance of Hider.
        """
        self.letterinput = letter
    

# GETTER
    @property
    def letterinput(self):
        return self._letterinput 

# SETTER
    @letterinput.setter

    def letterinput (self, guessedLetter):
        self._letterinput = guessedLetter.lower()
        
        


'''''
    def get_letter(self):
        """Responsability to assign the letter string to the self._letterinput .

        Args:
            self (Hider): An instance of Hider.
        """
        return self._letterinput    
    

    def getletterplayer(self, guessedLetter):
        """Responsability to get letter string and change to lower function and assign self._letterinput .

        Args:
            self (Hider): An instance of Hider.
        """
        
        self._letterinput = guessedLetter.lower()
        return self._letterinput
        
'''