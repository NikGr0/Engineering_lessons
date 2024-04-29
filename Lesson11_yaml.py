

class User:
    def __init__(self):
        self.d_user = [{'name': 'Ivan',
                  'age': '28',
                  'e_mail': 'ivan@mail.com'},
                 {'name': 'Petr',
                  'age': '33',
                  'e_mail': 'petr@mail.com'}]

    def get_data(self):
        return self.d_user


user1 = User()
#print(user1.get_data())


import yaml


with open('user_y.yaml', 'w') as file:
    documents = yaml.dump(user1.get_data(), file)

with open('user_y.yaml') as file:
    doc = yaml.load(file, Loader=yaml.FullLoader)
    print(doc)
