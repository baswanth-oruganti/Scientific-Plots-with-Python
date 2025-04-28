#!/usr/bin/env python
# coding: utf-8

# ### Loading of required modules

# In[103]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import FormatStrFormatter as Formatter
import matplotlib.ticker as ticker


# ### Loading data into a dataframe

# In[105]:


df_cond=pd.read_csv("conductivity.csv")
df_cond


# ### Create an empty frame for plotting

# In[109]:


fig, ax = plt.subplots(nrows=1,ncols=1,figsize=(5,4))
fig


# ### Define x and y values

# In[77]:


x=df_cond["volume_NaOH(mL)"]
y=df_cond["conductance(mS)"]
y


# ### Plotting

# In[88]:


ax.plot(x,y, marker="o",color="black")
fig


# ### Axes limits and labels
# 1. Define the axes limits using set_xlim and set_ylim functions
# 2. label the axes using set_xlabel, set_ylabel functions

# In[89]:


ax.set_xlim(0,12.2)
ax.set_ylim(0,30)
ax.set_xlabel('Vol of NaOH added (mL)')
ax.set_ylabel("conductivity(mS)")
fig


# ### Number Formats and Minor Tick Labels
# 1. Next, we want to have 1 decimal place in the X-axis values and zero decimal places in the Y-axis values. For this purpose we use formatter function.
# 2. We would like to have minor tick lables in the plot. For this purpose, we use set_minor_locator function.

# In[94]:


ax.xaxis.set_major_formatter(Formatter('%.1f'))
ax.yaxis.set_major_formatter(Formatter('%.2f'))

ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(2.5))
fig


# ### Figure layout and saving

# In[95]:


fig.tight_layout()
fig.savefig('conductivity.pdf',dpi=300)


# ### Determine end point

# In[99]:


min_cond=df_cond[df_cond['conductance(mS)']==df_cond['conductance(mS)'].min()]
min_cond


# In[ ]:




