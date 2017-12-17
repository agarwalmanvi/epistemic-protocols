###############################################################################
#                                                                             #
#  LEXER                                                                      #
#                                                                             #
###############################################################################

# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
ATOM, IMP, EOF = (
    'ATOM', 'IMP', 'EOF'
)

class Token(object):
    def __init__(self, type, value):
		# Token type: ATOM, IMP, or EOF
        self.type = type
		# Token value: digits, alphabets, '>'
        self.value = value

    def __str__(self):
        """String representation of the class instance.
        Examples:
            Token(ATOM, p2)
            Token(IMP, '>')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
		return self.__str__()
		
class Interpreter(object):
	def __init__(self, text):
		# input string
		self.text = text
		# self.pos is an index into self.text
		self.pos = 0
		# current token position 
		self.current_char
		
	def error(self):
		raise Exception('Error parsing input')
		
	def get_next_token(self):
		"""Breaks the sentence into tokens. One token at a time."""
		
		if self.pos > len(self.text)-1:
			return Token(EOF, None)
			
		current_char = self.text[self.pos]
		
		if current_char.isdigit() or current_char.isalpha():
			
		
			
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
