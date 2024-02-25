record = ['01302', 'esmartdata', ['python', 'sql', 'git', 'css'], 30000]
for i in record:
    if isinstance(i, list):
        i.clear()
print(record)