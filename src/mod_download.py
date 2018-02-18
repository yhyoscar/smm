import pandas as pd
import numpy as np
import sys
import os
import time
from datetime import datetime, timedelta

path_companylist = 'https://129.49.67.246/stock/companylist/'
path_histdata = 'https://129.49.67.246/stock/histdata/daily/'

# list of capital strings to numbers
def capstr2num(caplist):
    num = []
    for str in caplist:
        if str[0] == '$':
            unit = 1.0
            if str[-1] == 'B': unit = 1e9
            if str[-1] == 'M': unit = 1e6
            if str[-1] == 'K': unit = 1e3
            num.append(float(str[1:-1]) * unit)
        else:
            num.append( np.nan )
    return num

# list of IOP strings to years
def ipostr2num(slist):
    num = []
    for str in slist:
        if 'n' in str:
            num.append( np.nan )
        else:
            num.append(int(str))
    return num

# get the indexes of corresponding sectors
def gathersector(seclist):
    num = {}
    index = {}
    i = 0
    for s0 in seclist:
        s = s0.strip()
        if s in num.keys(): num[s] += 1; index[s].append(int(i))
        else:  num[s] = 1; index[s] = [int(i)]
        i += 1
    return index, num

# get the symbol list from the company list
def getsymlist(fcom='companylist_NASDAQ_20180214.csv'):
    comlist = pd.read_csv(path_companylist+fcom)
    comlist['cap']   =  capstr2num(comlist['MarketCap']) 
    comlist['ipo']   =  ipostr2num(comlist['IPOyear']) 
    secindex, secnum = gathersector(comlist['Sector'])
    print len(comlist['cap']), secnum
    return comlist

