'''
Created on Mar 12, 2018

@author: huzq85
'''

import os
import json
from pprint import pprint
from anaconda_navigator import static

class ParseConfigure(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
    
    @staticmethod
    def get_configure_data():
        parent_path = os.path.abspath(os.path.dirname(os.getcwd()))
        f_path = os.path.join(parent_path, "configure/Configure.json")
        with open(f_path) as data_file:
            data = json.load(data_file)
#         pprint(data)
        return data
    
    @staticmethod
    def __get_elem_web_url():
#         print(data['web'])
        data = ParseConfigure.get_configure_data()
        return data['web']
    
    @staticmethod
    def __get_elem_hist_data():
#         print(data['hist_data'])
        data = ParseConfigure.get_configure_data()
        return data['hist_data']
    
    @staticmethod
    def __get_elem_file_list():
#         print(data['fslist'])
        data = ParseConfigure.get_configure_data()
        return data['fslist']
    
    @staticmethod
    def __get_elem_all_exchanges():
        data = ParseConfigure.get_configure_data()
        return data['allexchanges']

    @staticmethod
    def __get_elem_dt_interval():
        data = ParseConfigure.get_configure_data()
        return data['dt_interval']
    
    @staticmethod
    def __get_elem_path_comp():
        data = ParseConfigure.get_configure_data()
#         print(data['comp_list'])
        return data['comp_list']
    
    @staticmethod
    def get_path_comp():
        return ParseConfigure.__get_elem_web_url() + ParseConfigure.__get_elem_path_comp()
    
    @staticmethod
    def get_path_data():
        return ParseConfigure.__get_elem_web_url() + ParseConfigure.__get_elem_hist_data() +ParseConfigure.__get_elem_dt_interval()
        
    @staticmethod
    def get_fslist():
        return ParseConfigure.get_path_data() +  ParseConfigure.__get_elem_file_list()

if '__main__' == __name__:
    print(ParseConfigure.get_path_comp())
    print(ParseConfigure.get_path_data())
    print(ParseConfigure.get_fslist())