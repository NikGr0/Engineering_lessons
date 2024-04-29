import yaml
import json


with open('user_y.yaml') as in_file, open('test_json.json', 'w') as out_file:
    doc = yaml.load(in_file, Loader=yaml.FullLoader)
    # print(doc[0])
    # print(type(doc[0]))
    j_object = json.dumps(doc[0], indent=4)
    print(j_object)
    out_file.write(j_object)