stocks = {
    'Technology Services': [
        'MSFT',
        'GOOG',
        'FB',
        'PYPL',
        'ABDE',
        'CSCO',
    ],
    'Retail Trade': ['AMZN', 'BABA', 'WMT', 'HD', 'SHOP'],
    'Electronic Technology': ['AAPL', 'TSM', 'NVDA'],
}

stocks_count = {key: len(value) for key, value in stocks.items()}

print(stocks_count)