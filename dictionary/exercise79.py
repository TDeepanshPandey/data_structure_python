dependencies = {
    'numpy': '1.20.1',
    'pandas': '1.2.3',
    'python-dateutil': '2.8.1',
    'pytz': '2021.1',
    'six': '1.15.0',
}

additional = {
    'cycler': '0.10.0',
    'kiwisolver': '1.3.1',
    'matplotlib': '3.4.1',
    'Pillow': '8.2.0',
    'pyparsing': '2.4.7',
}

all_dependencies = dependencies | additional

# all_dependencies = {**dependencies, **additional}

print(all_dependencies)