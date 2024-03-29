import numpy as np


np.set_printoptions(linewidth=160, suppress=True)

wig_games_raw = """Profile	Time	Course	Change	Change%	Ref.	Open	Low	High	Volume	Turn	Share
11B (11BIT)	17 kwi 17:01	391.00	+8.00	(+2.09%)	383.00	383.50	383.00	394.00	12 784	4 994 874	19.034%
CDR (CDPROJEKT)	17 kwi 17:01	339.50	+5.30	(+1.59%)	334.20	338.30	337.00	344.20	233 059	79 245 368	39.618%
CIG (CIGAMES)	17 kwi 17:03	0.742	-0.012	(-1.59%)	0.754	0.772	0.730	0.772	1 311 078	971 459	1.855%
PLW (PLAYWAY)	17 kwi 17:03	387.50	+18.00	(+4.87%)	369.50	374.00	373.00	388.00	33 206	12 661 786	10.638%
TEN (TSGAMES)	17 kwi 17:02	349.50	+22.50	(+6.88%)	327.00	332.00	330.00	353.50	39 793	13 697 060	28.855%"""

lines = wig_games_raw.splitlines()
lines = [line.split('\t') for line in lines]
wig_games = np.array(lines, dtype=np.str)
wig_games = np.char.replace(wig_games, ' ', '')
print(wig_games)