#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 13:21:17 2020

@author: vibinscat
"""
%matplotlib inline
import pandas as pd
import numpy as np
from datetime import datetime


df  = pd.read_csv('Columbus_Ed_astro_pi_datalog.csv', index_col=('ROW_ID'))
df2 = pd.read_csv('Columbus2_Ed_astro_pi_datalog.csv', index_col=('ROW_ID'))

columbus_data = pd.concat([df,df2])

list_timestamp = columbus_data['time_stamp']

new_col = []

for items in list_timestamp:
    new_col.append(datetime.strptime(items[0:10],"%Y-%m-%d"))



date_col = pd.Series(new_col)

columbus_data['Date'] = date_col

columbus_data.columns
