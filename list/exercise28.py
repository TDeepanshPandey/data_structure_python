raw_text = """Python is a programming language that lets you work more quickly 
and integrate your systems more effectively. You can learn to use Python and 
see almost immediate gains in productivity and lower maintenance costs. The 
mission of the Python Software Foundation is to promote, protect, and advance 
the Python programming language, and to support and facilitate the growth of 
a diverse and international community of Python programmers."""

tokens = raw_text.split()
tokens = [token.replace('.', '').replace(',', '') for token in tokens]
tokens = [token.lower() for token in tokens]
tokens = list(set(tokens))
tokens.sort()
tokens = [token for token in tokens if len(token) > 2]
tokens.sort(key=lambda x: len(x), reverse=True)
print(tokens[:8])