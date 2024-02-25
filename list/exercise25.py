raw_text = """Python is a programming language that lets you work more quickly 
and integrate your systems more effectively. You can learn to use Python and 
see almost immediate gains in productivity and lower maintenance costs. The 
mission of the Python Software Foundation is to promote, protect, and advance 
the Python programming language, and to support and facilitate the growth of 
a diverse and international community of Python programmers."""

tokens = raw_text.split()
tokens = [token.replace('.', '').replace(',', '').lower() for token in tokens]

print(tokens)