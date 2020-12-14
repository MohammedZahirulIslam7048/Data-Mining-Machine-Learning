#!/usr/bin/env python
# coding: utf-8

# In[46]:


import numpy as np
import statistics as st


# In[47]:


dataset01 = [1,2,3,4,5,7,9]


# In[48]:


dataset01


# In[49]:


dataset02 = [3, -7, 5, 13, -2]
#dataset02 = [3, 7, 5, 13, 2]


# In[50]:


dataset02


# # Mean

# In[51]:


mean1 = np.mean(dataset01)


# In[52]:


print('Mean for Dataset 01 = ',mean1)


# In[54]:


mean2 = np.mean(mean2)


# In[55]:


print('Mean for Dataset 02 = ',mean2)


# # Median

# In[56]:


median1 = np.median(dataset01)


# In[57]:


print('Median for Dataset 01 = ',median1)


# In[58]:


median2 = np.median(dataset02)


# In[59]:


print('Median for Dataset 02 = ', median2)


# # Mode (Not available in numpy)

# In[61]:


#mode1 = np.mode(dataset01)
#print('Mode for Dataset 02 = ', mode1)


# # Range

# In[62]:


range1 = np.max(dataset01) - np.min(dataset01)


# In[63]:


print('Range for Dataset 01 = ', range1)


# In[64]:


range2 = np.max(dataset02) - np.min(dataset02)


# In[65]:


print('Range for Dataset 02 = ', range2)


# In[ ]:




