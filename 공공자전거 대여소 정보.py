#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
CB = pd.read_csv('C:/Users/User/Downloads/공공자전거 대여소 정보(21.01.31 기준).csv', encoding='CP949', index_col=0, header=0, engine='python')
CB.head()


# In[7]:


addr = []
for address in CB.상세주소:
    addr.append(str(address).split())
addr 


# In[8]:


CB.to_csv('./bike_rental.csv', encoding = 'CP949', index = False) 


# In[20]:


CB_geoData = pd.read_csv('./bike_rental.csv', encoding = 'cp949', engine = 'python')


# In[21]:


import folium
map_CB = folium.Map(location = [37.560284, 126.975334], zoom_start = 15)


# In[22]:


for i, store in CB_geoData.iterrows():
     folium.Marker(location = [store['위도'], store['경도']], popup = store['보관소(대여소)명'], icon = folium.Icon(color = 'red',icon = 'star')).add_to(map_CB)


# In[23]:


map_CB.save('./map_CB.html')


# In[26]:


import webbrowser 
webbrowser.open('C:/Users/User/My_Python/map_CB.html')


# In[30]:


data = pd.read_csv('./bike_rental2.csv', index_col = 0, encoding = ' CP949', engine = 'python')
data.head()


# In[31]:


addr = pd.DataFrame(data['상세주소'].apply(lambda v: v.split()[:2]).tolist(), columns = ('시도', '군구'))
addr.head() 


# In[32]:


addr['군구'].unique()


# In[33]:


addr['시도군구'] = addr.apply(lambda r: r['시도'] + ' ' + r['군구'], axis = 1)
addr.head()   


# In[35]:


addr_group = pd.DataFrame(addr.groupby(['시도', '군구', '시도군구'], as_index = False).count())
addr_group.head()


# In[36]:


addr_group = addr_group.set_index("시도군구")
addr_group.head()


# In[40]:


population = pd.read_excel('C:/Users/User/My_Python/행정구역_시군구_별__성별_인구수_2.xlsx')
population.head() 


# In[41]:


population = population.rename(columns = {'행정구역(시군구)별(1)': '시도', '행정구역(시군구)별(2)': '군구'})
population.head() 


# In[45]:


for element in range(0,len(population)):
    population['군구'][element] = population['군구'][element].strip()
population['시도군구'] = population.apply(lambda r: r['시도'] + ' ' + r['군구'], axis = 1)
population.head()


# In[46]:


population = population[population.군구 != '소계']
population = population.set_index("시도군구")
population.head() 


# In[47]:


addr_population_merge = pd.merge(addr_group,population, how = 'inner', left_index = True, right_index = True)
addr_population_merge.head()


# In[48]:


local_MC_Population = addr_population_merge[['시도_x', '군구_x', 'count', '총인구수 (명)']]
local_MC_Population.head() 


# In[49]:


local_MC_Population = local_MC_Population.rename(columns = {'시도_x': '시도', '군구_x': '군구','총인구수 (명)': '인구수'})
MC_count = local_MC_Population['count']
local_MC_Population['MC_ratio'] = MC_count.div(local_MC_Population['인구수'], axis = 0)*100000
local_MC_Population.head()


# In[50]:


from matplotlib import pyplot as plt
from matplotlib import rcParams, style
style.use('ggplot')

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname = "c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family = font_name)


# In[51]:


MC_ratio = local_MC_Population[['count']]
MC_ratio = MC_ratio.sort_values('count', ascending = False)
plt.rcParams["figure.figsize"] = (25, 5)
MC_ratio.plot(kind = 'bar', rot = 90)
plt.show()


# In[52]:


MC_ratio = local_MC_Population[['MC_ratio']]
MC_ratio = MC_ratio.sort_values('MC_ratio', ascending = False)
plt.rcParams["figure.figsize"] = (25, 5)
MC_ratio.plot(kind = 'bar', rot = 90)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




