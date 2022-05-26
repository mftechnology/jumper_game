class Terminal:
    """
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """
     
    def read_input_text(self, prompt):
        """Get prompt to input on the screen
        """
        return input(prompt)

        
    def write_word(self, text):
        """To Display that text on the screen.
        """
        print(text)

    def write_same_line(self, text):
        """
        Display the text on the same line.
        """
        print(text, end = " ")
    
