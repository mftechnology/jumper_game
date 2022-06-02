from game.terminal import Terminal

class Parachute:
    """
    This class has the responsability to show parachute and remove character when the letter is wrong    
    """
        

    def __init__(self):
        """
        
        Atributes:
            self terminal a instance of Terminal Class
            self is_out_of_line : store Boolean like a True when find the last move as string "x"
            self parachute_list : a list to iniciate the parachute
        """
        self.terminal = Terminal()
        self.is_out_of_line = False
        self.parachute_list = [ "  ___   ", 
                                 " /___\\ ", 
                                 " \   /  ", 
                                 "  \ /   ", 
                                 "   O    ", 
                                 "  /|\\  ", 
                                 "  / \\  ", 
                                 "^^^^^^^^"
                                 ]
        

    def removeparachute(self):
        """
        To remove the first positions of parachute.
        Args:
            self (Parachute): An instance of Parachute.
        """
        if self.parachute_list[0] == "   x    ":
            self.is_out_of_line = True
        self.parachute_list.pop(0)

    def is_out_of_line(self):
        """
        To verify if were that last position for close
        Args:
            self (Parachute): An instance of Parachute.
        """
        
        if self.parachute_list[0] == "   x    ":
            self.is_out_of_line = True
        return self.is_out_of_line

    def show_parachute(self):
        """
        To show Parachute.
        Args:
            self (Parachute): An instance of Parachute.
        """
        
        self.terminal.write_word("")
        # To verify if the first position on parachute list is 0
        # If 0 replace for x for close game
        if self.parachute_list[0] == "   O    ":
            # replace first value
            self.parachute_list[0] = "   x    "
        
        #display on the screen
        for parachute in self.parachute_list:
            self.terminal.write_word(parachute)
    
       
    
    
