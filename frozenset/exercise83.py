dependencies = {
    ('numpy', '1.20.1'): 'installed',
    ('pandas', '1.2.3'): 'installed',
}

temp = {frozenset(key):value for key,value in dependencies.items()}

print(temp)