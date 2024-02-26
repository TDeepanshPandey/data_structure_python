aapl = {
    'ticker': 'AAPL',
    'company_name': 'APPLE INC',
    'P/E': 34.04,
    'EPS': 3.74,
    'employees': 147000,
}

msft = {
    'ticker': 'MSFT',
    'company_name': 'MICROSOFT CORP.',
    'P/E': 37.09,
    'EPS': 6.78,
    'employees': 163000,
}

"""table = (tuple(i for i in aapl.keys()), tuple(i for i in aapl.values()), tuple(i for i in msft.values()))"""

table = (tuple(aapl.keys()), tuple(aapl.values()), tuple(msft.values()))
print(table)