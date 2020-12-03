#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd
df1=pd.read_csv("C:\\Users\\DELL\\Downloads\\india-news-headlines.csv")
df2=pd.read_csv("C:\\Users\\DELL\\Downloads\\^GSPC.csv")


# In[47]:


df1


# In[48]:


df2


# In[49]:


type(df1['publish_date'][2])


# In[50]:


type(df2['Date'][1])


# In[20]:


#df1['publish_date'] = pd.to_datetime(df1['publish_date'], format='%Y-%m-%d') 


# In[51]:


from datetime import datetime
list1=[]
for i in df2['Date']:
    i= datetime.strptime(i, '%Y-%m-%d').date()
    list1.append(i)
df2['Date']=list1


# In[52]:


type(df2['Date'][1])


# In[27]:





# In[53]:


list2=[]
for i in df1['publish_date']:
    i= datetime.fromtimestamp(i).strftime('%Y-%m-%d')
    list2.append(i)
df1['publish_date']=list2


# In[54]:


type(df1['publish_date'][2])


# In[55]:


list3=[]
for i in df1['publish_date']:
    i= datetime.strptime(i, '%Y-%m-%d').date()
    list3.append(i)
df1['publish_date']=list3


# In[56]:


type(df1['publish_date'][2])


# In[57]:


df1 = df1.rename(columns={'publish_date': 'Date'})


# In[58]:


df1=df1.dropna(axis=0, inplace=False)


# In[59]:


len(df1.index)


# In[60]:


df2=df2.dropna(axis=0, inplace=False)


# In[61]:


len(df2.index)


# In[66]:


merged_df=df2.merge(df1,how='left', left_on='Date', right_on='Date')


# In[67]:


merged_df


# In[68]:


merged2=merged_df.dropna(axis=1)


# In[69]:


merged2


# In[70]:


merged_final=merged2.dropna()


# In[71]:


merged_final


# In[ ]:




