#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


canciones = pd.read_table('DATA/Corpus_rapv2.txt')
canciones.head()


# In[4]:


print(canciones.shape)


# In[7]:


print(canciones['chanson'].unique())

#Je ne sais pas comment donner le valeur de y


# In[113]:


corpus.drop('artiste', axis=1).plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False, figsize=(9,9), 
                                        title='Box Plot for each input variable')
plt.savefig('fruits_box')
plt.show()


# In[ ]:




