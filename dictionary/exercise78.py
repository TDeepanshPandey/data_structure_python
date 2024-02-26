eng_to_spa = {
    'one': 'uno',
    'two': 'dos',
    'three': 'tres',
    'four': 'cuatro',
    'five': 'cinco',
}

eng_to_number = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
}

spa_to_number = {i:j for i, j in zip(eng_to_spa.values(), eng_to_number.values())}

print(spa_to_number)
