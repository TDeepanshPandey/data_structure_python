countries = [
    'Turkey',
    'Russia',
    'United Kingdom',
    'Russia',
    'Germany',
    'Spain',
    'Ukraine',
    'Italy',
    'France',
    'Belarus',
]   

coun = []

for i in countries:
    coun.append(i.upper()[:3])

print(sorted(coun, key=lambda x: x[-1]))