#  tokenize expressions
import ply.lex as lex
all = """
abc * b
pq ** b
ab < bc + cd
p --- q
"""
tokens = ('ID', 'OP')

t_ignore = ' \t\n'

def t_ID(t) :
	r'[a-zA-Z]\w*'
	return t
def t_OP(t) :
	r'(--|-|\+|<|\*\*|\*)'
	return t
lexer = lex.lex()
lexer.input(all)
for t in lexer :
	print(t)


