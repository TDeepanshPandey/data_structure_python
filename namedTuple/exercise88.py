from collections import namedtuple

Client = namedtuple('Client',['client_id','type','discount'],defaults=[0])

client_1 = {'client_id': '239403', 'type': 'premium', 'discount': 0.1}
client_2 = {'client_id': '156513', 'type': 'economic'}
client_3 = {'client_id': '198433', 'type': 'standard'}

clients = [Client(**client_1),Client(**client_2),Client(**client_3)]

for client in clients:
    print(client)