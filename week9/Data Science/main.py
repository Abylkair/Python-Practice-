#!/usr/bin/env python
# coding: utf-8
# In[1]:
# импортируем библиотеки и модули
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
# In[2]:
# загружаем и визуализируем данные
# In[3]:
df = pd.read_excel('price1.xlsx')
# In[4]:
df
# In[12]:
get_ipython().run_line_magic('matplotlib', 'inline')

plt.scatter(df.area, df.price, color='red', marker='^')
plt.xlabel('площадь (кв.м.)')
plt.ylabel('стоимость (млн.руб)')
# In[13]:
# тренируем модель
# In[14]:
reg = linear_model.LinearRegression() #создали модель
# In[15]:
reg.fit(df[['area']],df.price) #обучаем модель на наших данных
# In[16]:
# предсказываем
# In[18]:
reg.predict([[120]])
# In[19]:
reg.predict(df[['area']])
# In[20]:
# Y = aX + b
# In[21]:
reg.coef_
# In[22]:
reg.intercept_
# In[23]:
# Стоимость = 0.07148238 * Площадь + 0.8111407046647887
# In[24]:
0.07148238 * 120 + 0.8111407046647887
# In[26]:
get_ipython().run_line_magic('matplotlib', 'inline')
plt.scatter(df.area, df.price, color='red', marker='^')
plt.xlabel('площадь (кв.м.)')
plt.ylabel('стоимость (млн.руб)')
plt.plot(df.area, reg.predict(df[['area']]))
# In[27]:
pred = pd.read_excel('prediction_price.xlsx')
# In[28]:
pred
# In[30]:
pred.head(3)
# In[32]:
p = reg.predict(pred) # предсказываем цены для новых квартир из нового файла
по нашей модели
# In[33]:
p
# In[34]:
# создаем новую колонку в файле с новыми квартирами и заносим туда
предсказанные цены
# In[35]:
pred['predicted prices'] = p
# In[36]
pred
# In[40]:
pred.to_excel('new.xlsx', index=False) # сохраняем файл в Excel без первой
колонки
