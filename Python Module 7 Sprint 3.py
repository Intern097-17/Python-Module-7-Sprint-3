#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from matplotlib import pyplot as plt


# In[ ]:


data = pd.read_csv('Data_ WHO Coronavirus Covid-19 Cases and Deaths - WHO-COVID-19-global-data.csv')


# In[ ]:


data


# In[ ]:


tc = data[data.TotalCase == 'Total Cases']


# In[ ]:


td = data[data.TotalDeath == 'Total Deaths']


# In[ ]:


td


# In[ ]:


plt.plot(tc.Dates_epicrv, tc.Dates_epicrv / 10**6)
plt.plot(td.Dates_epicrv, td.Dates_epicrv / 10**6)
plt.xLabel('time')
plt.yLabel('Those infected')
plt.legend(['Total Cases', 'Total Deaths'])
plt.show()


# In[ ]:




