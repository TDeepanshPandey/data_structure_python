countries = ('Germany', 'Spain', 'Italy', 'France', 'Romania', 'Austria', 'Poland')
cities = ('Berlin', 'Madrid', 'Rome', 'Paris', 'Bucharest', 'Vienna', 'Warsaw')
capital = zip(cities, countries)
for i,j in capital:
    print(j,'->',i)