#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 13:21:17 2020

@author: vibinscat
"""

import pandas as pd
import numpy as np
from datetime import datetime


df  = pd.read_csv('Columbus_Ed_astro_pi_datalog.csv')

list_timestamp = df['time_stamp']

new_col = []

for items in list_timestamp:
    new_col.append(datetime.strptime(items[0:10],"%Y-%m-%d"))

print(new_col)


date_col = pd.Series(new_col)

df['new_col'] = date_col
