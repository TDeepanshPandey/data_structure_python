user_1 = ('e_smartdata', 'e-smartdata.org', 477, 510, 'PL')
user_2 = ('krako', None, 412, 250, 'PL')
user_3 = ('pystar', None, 1406, 2400, 'US')
user_4 = ('py.learn', 'python.org', 1406, 2400, 'US')

users = (user_1, user_2, user_3, user_4)

websites = tuple(i[1] for i in users if i[1])
print(websites)