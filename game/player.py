
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
        self.letterinput =""

    def get_letter(self):
        return self.letterinput    

    def getletterplayer(self, guessedLetter):
        
        self.letterinput = guessedLetter.lower()
        return self.letterinput
        
