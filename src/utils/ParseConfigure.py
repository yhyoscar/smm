'''
Created on Mar 12, 2018

@author: huzq85
'''

import os
import json


class ParseConfigure(object):
    '''
    This class use for getting configuration data from json file
    '''
    
    def __init__(self):
        '''
        Constructor: To read data from json file
        #TODO: This constructor should be revised, it's better not to put config data reading
        # procedure in this constructor
        '''
        self.data = ''
        
        parent_path = os.path.abspath(os.path.dirname(os.getcwd()))
        f_path = os.path.join(parent_path, "configure/Configure.json")
        with open(f_path) as data_file:
            data = json.load(data_file)
        self.data = data
    
    def __get_elem_web_url(self):
        return self.data['web']
    
    def __get_elem_hist_data(self):
        return self.data['hist_data']
    
    def __get_elem_file_list(self):
        return self.data['fslist']
    
    def __get_elem_all_exchanges(self):
        return self.data['allexchanges']
    
    def __get_elem_dt_interval(self):
        return self.data['dt_interval']
    
    def __get_elem_path_comp(self):
        return self.data['comp_list']
    
    def get_path_comp(self):
        return self.__get_elem_web_url() + self.__get_elem_path_comp()
    
    def get_path_data(self):
        return self.__get_elem_web_url() + self.__get_elem_hist_data() + self.__get_elem_dt_interval()
    
    def get_fslist(self):
        return self.get_path_data() + self.__get_elem_file_list()


if '__main__' == __name__:
    parseConfig = ParseConfigure()
    print(parseConfig.get_path_comp())
    print(parseConfig.get_path_data())
    print(parseConfig.get_fslist())
