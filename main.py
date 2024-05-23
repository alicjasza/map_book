# name: str = input("Enter your name: ")
# print(f'WITAJ{name}')

data_of_users: list = [
    {'name': 'Alicja', 'surname': 'Szadura', 'posts': 5, 'location': 'Krasnystaw'},
    {'name': 'Norbert', 'surname': 'Szeliga', 'posts': 15, 'location': 'Rzeszów'},
    {'name': 'Kacper', 'surname': 'Wójcik', 'posts': 8, 'location': 'Legnica'},
    {'name': 'Sebastian', 'surname': 'Dudek', 'posts': 12, 'location': 'Siedlce'},
]
print(f'WITAJ {data_of_users[0]['name']}')
def read(users:list)->None:
    """
    this is a function to show users from an list
    :param users: a list of users
    :return: None
    """
    for user in users[1:]:
        print(f'Twój znajomy: {user['name']},opublikował :{user['posts']}')

read(data_of_users)