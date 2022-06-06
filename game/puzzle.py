
from game.terminal import Terminal
import random


class Puzzle:
    """
    Keep on secret the word sorted, and show the letters
    
    Attributes:
        self._sorted_word = random list with words
        self.letter_used = list to store the words that were stored
        self.character = list with the character "_" and with the letters insert to the user prompt
        self.wrong_guesses = count erros 
        self.terminal = instance of Terminal classes
        self.name_found = Bollean to verify if the word is founded
    """

    def __init__(self):
        """Constructs a new word.

        Args:
            self (puzzle): An instance of puzzle.
        """
        #self._sorted_word = random.choice( ["argument","baseball","bathroom","chemical","business","birthday","champion","artistic","children","aircraft"])
      
        self._sorted_word = ["argument","baseball","bathroom","chemical","business","birthday","champion","artistic","children","aircraft"]
        self.letter_used = []
        self.character = []
        self.wrong_guesses = 0
        self.terminal = Terminal()
        self.name_found = False
        

    #Getter
    @property
    def _sorted_word(self):
        
        return self._secret_word
    
    #Setter
    @_sorted_word.setter
    def _sorted_word(self, list_word):
        self._secret_word = random.choice(list_word )
        
        



    def isfound(self):
        """To verify if letter in secret word 

        Args:
            self (puzzle): An instance of puzzle.
        """ 
        self.terminal.write_word("")
        
        listword = list(self._secret_word)
        ind = 0 

        for i in listword:
            for l in self.letter_used:
                if i == l:
                    self.character[ind] = l
            ind += 1          
        
        self.terminal.write_word("")
        
        #show result on screen
        for space in self.character:
            self.terminal.write_same_line(space)

    def first_space_letters(self):
        """To show the first character of secret word

        Args:
            self (puzzle): An instance of puzzle.
        """ 
        
        self.terminal.write_word("")
        
        listword = list(self._secret_word)
        for i in listword:
            self.character.append("_")
           

    def getword(self, player, parachute):
        """the insert player and parachute class on
        parachute to remove and store letter_used list

        Args:
            self (puzzle): An instance of puzzle.
        """ 
        self.terminal.write_word("")

        print(player)
       
        if player not in self._secret_word:
            self.wrong_guesses += 1
            parachute.removeparachute()
        
        self.letter_used.append(player)
    

    def is_solved(self):
        """To verify is exist "_" on the list character.

        Args:
            self (puzzle): An instance of puzzle.
        """ 
        
        interator = 0
        
        for i in self.character:
            if i == "_":
                interator += 1
                self.name_found = False
           
        if interator == 0:
            self.name_found = True
        
        return self.name_found
                                                                    
     
 