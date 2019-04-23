#!/usr/bin/env python
# coding: utf-8

# In[18]:


marker_symbol = input ("Enter a gene symbol: ")


# In[19]:


import pandas as pd
CSV_URL = "https://www.ebi.ac.uk/mi/impc/solr/genotype-phenotype/select?q=marker_symbol:" + marker_symbol + "&rows=500&wt=csv&indent=1"
df = pd.read_csv(CSV_URL)
pd.unique(df['mp_term_name']).tolist()
print(CSV_URL)


# In[20]:


if df.empty:
    print("Looks like that gene doesn't have available information. Try another gene or check your cAsE.")
else:
    print ("The symbol you entered is valid")


# In[4]:


ParamId4Query = df.loc[df['mp_term_name'] ==  "decreased erythrocyte cell number", "parameter_stable_id"].iloc[0]


# In[5]:


ColonyId4Query = df.loc[df['mp_term_name'] ==  "decreased erythrocyte cell number", "colony_id"].iloc[0]


# In[6]:


CSV2_URL =  "https://www.ebi.ac.uk/mi/impc/solr/experiment/select?q=parameter_stable_id:IMPC_HEM_002_001%20AND%20colony_id:MEBV&rows=500&wt=csv&indent=true"
ControlURL = "https://www.ebi.ac.uk/mi/impc/solr/experiment/select?q=parameter_stable_id:IMPC_HEM_002_001%20AND%20colony_id:MEBV&indent=true&wt=csv&rows=1&fl=metadata_group,phenotyping_center,strain_accession_id"
ControlDataURL = "https://www.ebi.ac.uk/mi/impc/solr/experiment/select?q=parameter_stable_id:IMPC_HEM_002_001&wt=csv&fq=metadata_group:c5d5b3349a0014cdac742fb284d786ed&fq=phenotyping_center:WTSI&fq=strain_accession_id:%22MGI:2159965%22&fq=biological_sample_group:control&rows=100"


# In[7]:


import pandas as pd
df2 = pd.read_csv(CSV2_URL)
df2.info()

df3 = pd.read_csv(ControlDataURL)
df3.info()


# In[8]:


df2.groupby(['biological_sample_group', 'sex'])[['data_point']].mean()


# In[11]:


import matplotlib.pyplot as plt
x = df2['date_of_experiment']
y = df2['data_point']
plt.scatter(x,y)
plt.show()


# In[12]:


import seaborn as sns
x = df2['date_of_experiment']
y = df2['data_point']
sns.catplot(x = 'sex', y = 'data_point', col = 'biological_sample_group', kind = 'bar', data=df2)
plt.show()


# In[ ]:




