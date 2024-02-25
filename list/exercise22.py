population = [
    ('Istanbul', 'Turkey', 15462452),
    ('Moscow', 'Russia', 12195221),
    ('London', 'United Kingdom', 9126366),
    ('Saint Petersburg', 'Russia', 5383890),
    ('Berlin', 'Germany', 3748148),
    ('Madrid', 'Spain', 3223334),
    ('Kyiv', 'Ukraine', 2950800),
    ('Rome', 'Italy', 2844750),
    ('Paris', 'France', 2140526),
    ('Minsk', 'Belarus', 1982444),
]

a = [idx for idx, val in enumerate(population) if val[0]=='Kyiv'][0]
b= list(population[a])
b[0] = 'Kiev'
b = tuple(b)
population[a] = b
for row in population:
    print(row)