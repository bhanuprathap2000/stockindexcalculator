# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 20:16:57 2020

@author: Bhanu
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 17:21:14 2020

@author: Bhanu
"""

import datetime
import yfinance as yf
import pandas as pd
import math
import numpy as np



def indexrangecal(index,spotvalue_index,timetoexpiry):
    if index=="nifty":
        stock=yf.Ticker("^NSEI")
        df=stock.history(period='max')
        df.drop(["Volume","Dividends","Stock Splits"],inplace=True,axis=1)
    else:
        stock=yf.Ticker("^NSEBANK")
        df=stock.history(period='max')
        df.drop(["Volume","Dividends","Stock Splits"],inplace=True,axis=1)
    df["logreturn"]=np.log(df["Close"]/df["Close"].shift(1))
    standarddeviation=df.std()
    dstdev=standarddeviation["logreturn"]
    indexpos1sd=round((spotvalue_index+spotvalue_index*dstdev*math.sqrt(timetoexpiry)))
    indexpos2sd=round((spotvalue_index+2*spotvalue_index*dstdev*math.sqrt(timetoexpiry)))
    indexneg1sd=round((spotvalue_index-spotvalue_index*dstdev*math.sqrt(timetoexpiry)))
    indexneg2sd=round((spotvalue_index-2*spotvalue_index*dstdev*math.sqrt(timetoexpiry)))
    return indexneg1sd,indexpos1sd,indexneg2sd,indexpos2sd
  

    
    


