stocks = {
    'Facebook': 306.26,
    'Amazon': 3223.82,
    'Apple': 126.21,
    'Netflix': 544.53,
    'Alphabet': 2209.26,
    'Microsoft': 247.86
}

usdpln = 3.8

stocks_pln = {i: round(stocks[i]*usdpln,2) for i in stocks.keys() }

print(stocks_pln)