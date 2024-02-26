stocks = {
    'Facebook': 306.26,
    'Amazon': 3223.82,
    'Apple': 126.21,
    'Netflix': 544.53,
    'Alphabet': 2209.26,
    'Microsoft': 247.86
}

result = {key:value for key, value in stocks.items() if value >= 1000}

print(result)