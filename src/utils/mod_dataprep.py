import numpy as np
import pandas as pd
import requests
import os
from datetime import datetime, timedelta
from configure import *

#============================================================
def checkexist(symbol='GOOG'):
    slist = pd.read_csv(fslist)
    if symbol in slist['Symbol'].values:
        if slist[slist['Symbol'] == symbol]['Exist'].values[0] == 1:
            return True
        else:
            print('ERROR: data of', symbol, 'does not exist!')
            return False
    else:
        print('ERROR:', symbol, 'does not exsit!')
        return False    

def getonequote(symbol='GOOG'):
    if checkexist(symbol):
        url = path_data+symbol+'/'+symbol+'.csv'
        rtest = requests.get(url, allow_redirects=False)
        if rtest.status_code == 200:
            quote = pd.read_csv(path_data+symbol+'/'+symbol+'.csv')
            quote.symbol = symbol
            return quote
        else:
            print('ERROR:', symbol, 'does not exist in the database!')
            return None
    else:
        return None

def getmulquote(symbol = ['GOOG', 'MS']):
    quotes = {s:getonequote(s) for s in symbol}
    return quotes    
    
def getinfo_onequote(symbol='GOOG'):    
    pdflist = pd.read_csv(fslist)
    if symbol in pdflist['Symbol'].values:
        exchange = pdflist[pdflist['Symbol']==symbol]['Exchange'].values[0]
        pdcomp = pd.read_csv(path_comp+'companylist_'+exchange+'.csv')
        info = pdcomp[pdcomp['Symbol'] == symbol]
        info = info.merge(pdflist[pdflist['Symbol']==symbol])
        return info[['Exchange','Symbol','Name','Exist','LastSale',\
                     'MarketCap','IPOyear','Sector','industry',\
                     'Start_date', 'End_date']]
    else:
        print('ERROR:', symbol, 'does not exsit!')
        return None

def getinfo_mulquote(symbol=['GOOG', 'MS']):
    infos = None
    for s in symbol:
        info = getinfo_onequote(s)
        print( s, end=', ')
        if infos is None:
            infos = info
        else:
            if not (info is None):
                infos = infos.append(info)
    return infos    
    
def clean_null(quote, term='Adj Close'):
    print('cleanning null data ...')
    ntime0 = len(quote)
    quote = quote[quote[term] != 'null']
    ntime  = len(quote)
    if ntime0 > ntime:
        print('null data: ', ntime0 - ntime)
        print('valid data: ', ntime)
    return quote

def add_datetime(quote):
    quote.loc[:, 'datetime'] = [datetime(int(s[0:4]), int(s[5:7]), int(s[8:10]) ) for s in quote['Date']]
    return quote

def add_logreturn(quote, n=[0, 1]):
    # n --- 0: in-day logreturn (Close/Open); 
    #       1: 1-day logreturn (Adj Close); 
    #       k: k-day logreturn (Adj Close)
    if 'null' in quote['Close'].values:
        quote = clean_null(quote)
    ntime = len(quote)
    logadj = np.array( np.log( quote.loc[:,'Adj Close'].astype('float') ))
    for i in n:
        quote.loc[:,'logreturn_'+format(i)] = np.zeros([ntime])
        if i==0:
            quote.loc[:,'logreturn_0'] = np.log(quote.loc[:, 'Close'].astype('float'))  - \
                np.log(quote.loc[:, 'Open'].astype('float')) 
        else:
            #quote['logreturn_'+format(i)].values[i:ntime] = logadj[i:ntime] - logadj[0:ntime-i]
            quote.loc[quote.index[i:ntime], 'logreturn_'+format(i)] = logadj[i:ntime] - logadj[0:ntime-i]
    return quote

def capstr2num(capstr):
    if capstr is np.nan:
        return np.nan
    else:
        if capstr[0] == '$':
            unit = 1.0
            if capstr[-1] == 'B': unit = 1.0e9
            if capstr[-1] == 'M': unit = 1.0e6
            if capstr[-1] == 'K': unit = 1.0e3
            return float(capstr[1:-1]) * unit
        else:
            return np.nan
