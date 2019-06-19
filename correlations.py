# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 00:21:11 2019

@author: nshal
"""

import pandas as pd
import matplotlib.pyplot as plt

SP500 = pd.read_csv(r'C:\Users\nshal\Desktop\TrumpS&P\SP500.csv')
Trump = pd.read_csv(r'C:\Users\nshal\Desktop\TrumpS&P\approval_topline.csv')

Trump_voters = Trump.loc[Trump['subgroup']=='Voters']

SP500['SP500'] = pd.to_numeric(SP500['SP500'],errors='coerce')


SP500['SP500'] = SP500['SP500'].fillna(method='pad')


SP500['Norm'] = (SP500['SP500']-SP500['SP500'].mean())/SP500['SP500'].std()
Trump_voters['Norm'] = (Trump_voters['approve_estimate']-Trump_voters['approve_estimate'].mean())/Trump_voters['approve_estimate'].std()

SP500['DATE'] = pd.to_datetime(SP500['DATE'])
Trump_voters['modeldate'] = pd.to_datetime(Trump_voters['modeldate'])

plt.plot(SP500['DATE'], SP500['Norm'])
plt.plot(Trump_voters['modeldate'], Trump_voters['Norm'])
plt.show()


Trump_voters['Norm'].corrwith(SP500['Norm'])