from collections import namedtuple
User = namedtuple('User', ['user_id','nick','email','level'])

users = [User('0120', 'mike', 'mike@smartdata.org',30),
         User('3246', 'john', 'john@smartdata.org',52),
         User('1658', 'steve', 'steve@smartdata.org',10)]

users.sort(key=lambda user: user.level)

for user in users:
    print(user)

