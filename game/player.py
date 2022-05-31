
from numpy import seterr


class Player:
    """ A person who insert letter to the game. 

    Attributes:
        
        self.letterinput (String) with the letter input

    """

    def __init__(self):
        """Constructs a new Hider.

        Args:
            self (Hider): An instance of Hider.
        """
        self._letterinput =""
    
   
    def get_letter(self):
        return self._letterinput    
    
  
    def getletterplayer(self, guessedLetter):
        
        self._letterinput = guessedLetter.lower()
        return self._letterinput
        
