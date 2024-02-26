from collections import namedtuple
User = namedtuple('User', ['user_id','nick','email'])

users = (User('0120', 'mike', 'mike@smartdata.org'),
         User('3246', 'john', 'john@smartdata.org'),
         User('1658', 'steve', 'steve@smartdata.org'))
for i in users:
    print(i.nick,'->',i.email)
