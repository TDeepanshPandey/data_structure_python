from collections import namedtuple


User = namedtuple(
    typename='User',
    field_names=['user_id', 'nick', 'email', 'level'],
)

user_1 = {
    'user_id': '0120',
    'nick': 'mike',
    'email': 'mike@smartdata.org',
    'level': 30,
}
user_2 = {
    'user_id': '3246',
    'nick': 'john',
    'email': 'john@smartdata.org',
    'level': 52,
}
user_3 = {
    'user_id': '1658',
    'nick': 'steve',
    'email': 'steve@smartdata.org',
    'level': 10,
}

users = [User(**user_1),User(**user_2),User(**user_3)]

for user in users:
    print(f'{user.user_id},{user.email}')