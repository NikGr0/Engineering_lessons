import json


d = {'name': 'Ivan',
     'age': '28',
     'e_mail': 'ivan@mail.com'}

json_object = json.dumps(d, indent=4)

with open('sample.json', 'w') as file:
    file.write(json_object)

with open('sample.json') as file:
    json_object = json.load(file)
    print(json_object)
#print(d)