user_ids = ['0111', '0101', '1030', '0101', '3401', '0111', '1001']
user_id = '1040'
try: 
    user_ids.remove('1040')
except ValueError:
    print("User with id '{}' is not in the list.".format(user_id))