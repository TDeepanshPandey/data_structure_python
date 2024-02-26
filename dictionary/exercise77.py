eng_to_spa = {
    'one': 'uno',
    'two': 'dos',
    'three': 'tres',
    'four': 'cuatro',
    'five': 'cinco',
}

spa_to_eng = {values:key for key,values in eng_to_spa.items()}

print(spa_to_eng)