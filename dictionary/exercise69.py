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

stocks = {aapl['ticker']:[aapl[i] for i in aapl.keys() if i != 'ticker'],
          msft['ticker']:[msft[i] for i in msft.keys() if i != 'ticker']}

print(stocks)