import os
import json
from pprint import pprint

def get_confingure_data():
    parent_path = os.path.abspath(os.path.dirname(os.getcwd()))
    f_path = os.path.join(parent_path, "configure\Configure.json")
    with open(f_path) as data_file:
        data = json.load(data_file)
    pprint(data)
    return data


# if '__main__' == __name__:
#     # parent_path = os.path.abspath(os.path.dirname(os.getcwd()))
#     # f_path = os.path.join(parent_path, "Configure\Configure.json")
#     # print (f_path)
#     get_confingure_data()
