countries = (
    'Germany',
    'Spain',
    'Italy',
    'France',
    'Romania',
    'Austria',
    'Poland',
)

remove_idx = countries.index('Romania')
countries = countries[:remove_idx]+countries[remove_idx+1:]
print(countries)