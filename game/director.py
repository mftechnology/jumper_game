from game.terminal import Terminal
from game.puzzle import Puzzle
from game.player import Player
from game.parachute import Parachute


class Director:
    """A person who directs the game. 

    Attributes:
        
        is_playing (boolean): Whether or not to keep playing.
        self._puzzle = an instance of Puzzle()
        self.terminal = an instance of Terminal()
        self.player = an instance of  Player()
        self.parachute = an instance of Parachute()

    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        self._puzzle = Puzzle()
        self.terminal = Terminal()
        self.player = ("")
        self.parachute = Parachute()
     
        
        
    def start_game(self):
        """Starts the game.
    
           Args:
            self (Director): An instance of Director.
        """
        self.terminal.write_word("========= START GAME ============")
        self.fist_space_letters()
        self.getpuzzle()
        self.showparachute() 
        
        """Call the main methods of the Director class.
        """
        while self.is_playing:
            self.inputs()
            self.make_updates()
            self.getpuzzle ()            
            self.showparachute()            
            self.end_game()
    
    def fist_space_letters(self):
        """ Show len of word secret as "_".
    
           Args:
            self (Director): An instance of Director.
        """
        self._puzzle.first_space_letters()


    def getpuzzle(self):
        """To verify if letter in secret word.

        Args:
            self (Director): An instance of Director.
        """
        self._puzzle.isfound()


    def showparachute(self):
        """
        Display the Parachute.
        
        Args:
            self (Director): An instance of Director.
        """
        self.parachute.show_parachute()
        
    
    def inputs(self):
        """Get the string of user letter and assign to variable to pass class Player.

        Args:
            self (Director): An instance of Director.
        """
        letter = self.terminal.read_input_text("\nGuess a letter [a-z]: ")

       # self.player.getletterplayer(letter)
        letter = Player(letter)
        self.player = letter._letterinput

        return self.player
        
        
    
    def make_updates(self):
        """
        Call getword of Class Puzzle and insert Player and Parachute.
        
        Args:
            self (Director): An instance of Director.
        """
        self._puzzle.getword(self.player,self.parachute)
   
    def end_game(self):
        """
        To verify if game is finished.
        
        Args:
            self (Director): An instance of Director.
        """
        # Check parachute
        
        if self.parachute.is_out_of_line == True:
          self.is_playing = False
          self.terminal.write_word("------- Game Over: You Loose -------")
        
        # Check if secret word has solved 
        if self._puzzle.is_solved():
            print(self._puzzle.name_found)
            self.is_playing = False
            self.terminal.write_word("-------  Thanks for playing! -------") 
        
    