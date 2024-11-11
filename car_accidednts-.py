#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.subplots as sp
import plotly.express as px


# In[2]:


df = pd.read_csv('accidents_2017_to_2023_english.csv')
df.head()


# In[3]:


df.isnull().sum()


# In[4]:


df.dtypes


# In[5]:


#transformar em data 
df['inverse_data'] = pd.to_datetime(df['inverse_data'])
df.head()


# In[6]:


#acrescentando coluna ano
df['year'] = df['inverse_data'].dt.year
df.head()


# In[7]:


#acrescentando mes
df['month'] = df['inverse_data'].dt.month
df.head()


# In[8]:


#number of accidents per year
accidents_year = df['year'].value_counts().reset_index()
accidents_year.columns = ['year','count']

#number of accidents per month
accidents_month = df['month'].value_counts().reset_index()
accidents_month.columns = ['month','count']

#number of accidents per week
day_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] 
df['week_day'] = pd.Categorical(df['week_day'],categories=day_week,ordered=True)
accidents_week = df['week_day'].value_counts().reset_index() 
accidents_week.columns = ['week_day','count']
accidents_week = accidents_week.sort_values('week_day')

#number of accidents per hour
df['hour'] = pd.to_datetime(df['hour'], format='%H:%M:%S', errors='coerce').dt.hour
accident_time = df['hour'].value_counts().reset_index()
accident_time.columns = ['hour','count']


# In[9]:


fig = sp.make_subplots(rows=2, cols=2, subplot_titles=(
    "Year",
    "Month",
    "Weekday",
    "Hour"
))

# year
fig.add_trace(px.bar(accidents_year, x='year', y='count').data[0], row=1, col=1)
# month
fig.add_trace(px.bar(accidents_month, x='month', y='count').data[0], row=1, col=2)
# week
fig.add_trace(px.bar(accidents_week, x='week_day', y='count').data[0], row=2, col=1)
# time
fig.add_trace(px.bar(accident_time, x='hour', y='count').data[0], row=2, col=2)

# Ajuste do layout e margens para alinhar os gráficos à esquerda
fig.update_layout(
    title_text="Number of Accident per time",
    showlegend=False,
    height=600,
    width=700,
    margin=dict(l=10, r=10, t=90, b=10)  # Ajuste de margem esquerda (l) e direita (r)
)

# Show the plot
fig.show()


# In[10]:


#number of accidents per state
accidents_state = df['state'].value_counts().reset_index()
accidents_state.columns = ['state','count']
top10_accidents_state = accidents_state.nlargest(10,'count')

#number of accidents per city
accidents_city = df['city'].value_counts().reset_index()
accidents_city.columns = ['city','count']
top10_accidents_city = accidents_city.nlargest(10,'count')


# In[11]:


fig = sp.make_subplots(rows=1, cols=2, subplot_titles=(
    "Number of Accidents per State",
    "Number of Accidents per City",
    ))

#state
fig.add_trace(px.bar(top10_accidents_state, x='state', y='count').data[0], row=1, col=1)
# city
fig.add_trace(px.bar(top10_accidents_city, x='city', y='count').data[0], row=1, col=2)


# In[12]:


#number of accidents per weather_timestamp
accidents_weather_timestamp = df['weather_timestamp'].value_counts().reset_index()
accidents_weather_timestamp.columns = ['weather_timestamp','count']

#number of accidents per wheather_condition
accidents_wheather_condition = df['wheather_condition'].value_counts().reset_index()
accidents_wheather_condition.columns = ['wheather_condition','count']


# In[13]:


fig = sp.make_subplots(rows=1, cols=2, subplot_titles=(
    "Number of Accidents per Weather Timestamp",
    "Number of Accidents per Wheather Condition",
    ))

#accidents_weather_timestamp
fig.add_trace(px.bar(accidents_weather_timestamp, x='weather_timestamp', y='count').data[0], row=1, col=1)
# accidents_wheather_condition
fig.add_trace(px.bar(accidents_wheather_condition, x='wheather_condition', y='count').data[0], row=1, col=2)


# In[14]:


#number of accidents per road_type
accidents_road_type = df['road_type'].value_counts().reset_index()
accidents_road_type.columns = ['road_type','count']

#number of accidents per road_delineation
accidents_road_delineation = df['road_delineation'].value_counts().reset_index()
accidents_road_delineation.columns = ['road_delineation','count']

#number of accidents per road_direction
accidents_road_direction = df['road_direction'].value_counts().reset_index()
accidents_road_direction.columns = ['road_direction','count']


# In[15]:


fig = sp.make_subplots(rows=2, cols=2, subplot_titles=(
    "Road Type",
    "Road Delineation",
    "Road Direction"
    ))

#accidents_weather_timestamp
fig.add_trace(px.bar(accidents_road_type, x='road_type', y='count').data[0], row=1, col=1)
# accidents_road_delineation
fig.add_trace(px.bar(accidents_road_delineation, x='road_delineation', y='count').data[0], row=1, col=2)
# accidents_road_direction
fig.add_trace(px.bar(accidents_road_direction, x='road_direction', y='count').data[0], row=2, col=1)

fig.update_layout(
    title_text="Number of Accident by Road",
    showlegend=False,
    height=600,
    width=700,
    margin=dict(l=10, r=10, t=90, b=10)  # Ajuste de margem esquerda (l) e direita (r)
)


# In[16]:


#number of accidents per cause_of_accident
cause_of_accident = df['cause_of_accident'].value_counts().reset_index()
cause_of_accident.columns = ['cause_of_accident','count']
top10_cause_of_accident = cause_of_accident.nlargest(10,'count')

#number of accidents per type_of_accident
type_of_accident = df['type_of_accident'].value_counts().reset_index()
type_of_accident.columns = ['type_of_accident','count']
top10_type_of_accident = type_of_accident.nlargest(10,'count')


# In[17]:


fig = sp.make_subplots(rows=1, cols=2, subplot_titles=(
    "Number of Accidents per Cause of Accident",
    "Number of Accidents per Type of Accident",
    ))

#accidents_weather_timestamp
fig.add_trace(px.bar(top10_cause_of_accident, x='cause_of_accident', y='count').data[0], row=1, col=1)
# accidents_wheather_condition
fig.add_trace(px.bar(top10_type_of_accident, x='type_of_accident', y='count').data[0], row=1, col=2)

fig.update_layout(
    showlegend=False,
    height=600,
    width=700,
    margin=dict(l=10, r=10, t=90, b=10)  # Ajuste de margem esquerda (l) e direita (r)
)


# In[18]:


death_victims = df[df['victims_condition']=="With dead victims"]
death_weather_timestamp = (death_victims['weather_timestamp'].value_counts()/df['weather_timestamp'].value_counts())*100
death_weather_timestamp_df = death_weather_timestamp.reset_index()
death_weather_timestamp_df.columns = ['weather_condition', 'percentage']


# In[19]:


death_weather_timestamp_df = death_weather_timestamp.reset_index()
death_weather_timestamp_df.columns = ['weather_condition', 'percentage']  # Renomeia as colunas para clareza

# Criando o gráfico de barras
fig = px.bar(
    death_weather_timestamp_df, 
    x='weather_condition', 
    y='percentage', 
    title="Percentage of Fatal Accidents by Weather Condition (%)",
    labels={'weather_condition': 'Weather Condition', 'percentage': 'Percentage (%)'}
)

# Exibindo o gráfico
fig.show()


# In[20]:


death_victims = df[df['victims_condition']=="With dead victims"]

#death per year
death_year = (death_victims['year'].value_counts()/df['year'].value_counts())*100
death_year = death_year.reset_index()
death_year.columns = ['death_year', 'percentage']

#death per month
death_month = (death_victims['month'].value_counts()/df['month'].value_counts())*100
death_month = death_month.reset_index()
death_month.columns = ['death_month', 'percentage']

#death per week

day_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] 
death_victims['week_day'] = pd.Categorical(death_victims['week_day'],categories=day_week,ordered=True)
death_week = (death_victims['week_day'].value_counts()/df['week_day'].value_counts())*100
death_week = death_week.reset_index()
death_week.columns = ['week_day','percentage']
death_week = death_week.sort_values('week_day')

#death per week hour
death_hour = (death_victims['hour'].value_counts()/df['hour'].value_counts())*100
death_hour = death_hour.reset_index()
death_hour.columns = ['hour','percentage']


# In[21]:


fig = sp.make_subplots(rows=2, cols=2, subplot_titles=(
    "Year",
    "Month",
    "Week",
    "Hour"
    ))

#accidents_weather_timestamp
fig.add_trace(px.bar(death_year, x='death_year', y='percentage').data[0], row=1, col=1)
# accidents_wheather_condition
fig.add_trace(px.bar(death_month, x='death_month', y='percentage').data[0], row=1, col=2)
#accidents_wheather_condition
fig.add_trace(px.bar(death_week, x='week_day', y='percentage').data[0], row=2, col=1)
#accidents_wheather_condition
fig.add_trace(px.bar(death_hour, x='hour', y='percentage').data[0], row=2, col=2)


fig.update_layout(
    title_text="Percentage of Fatal Accidents by Time (%)",
    showlegend=False,
    height=600,
    width=700,
    margin=dict(l=10, r=10, t=90, b=10)  # Ajuste de margem esquerda (l) e direita (r)
)


# In[22]:


#death per state
death_state = (death_victims['state'].value_counts()/df['state'].value_counts())*100
death_state = death_state.reset_index()
death_state.columns = ['death_state', 'percentage']
top10_death_state = death_state.nlargest(10,'percentage')


# In[23]:


fig = sp.make_subplots(rows=1, cols=2, subplot_titles=(
    "% Fatal Accidents by State",
          ))

#accidents_weather_timestamp
fig.add_trace(px.bar(top10_death_state, x='death_state', y='percentage').data[0], row=1, col=1)

fig.update_layout(
    showlegend=False,
    height=600,
    width=700,
    margin=dict(l=10, r=10, t=90, b=10)  # Ajuste de margem esquerda (l) e direita (r)
)


# In[24]:


#death per weather_timestamp
death_weather_timestamp = (death_victims['weather_timestamp'].value_counts()/df['weather_timestamp'].value_counts())*100
death_weather_timestamp = death_weather_timestamp.reset_index()
death_weather_timestamp.columns = ['death_weather_timestamp', 'percentage']

#death per wheather_condition
death_wheather_condition = (death_victims['wheather_condition'].value_counts()/df['wheather_condition'].value_counts())*100
death_wheather_condition = death_wheather_condition.reset_index()
death_wheather_condition.columns = ['death_wheather_condition', 'percentage']


# In[25]:


fig = sp.make_subplots(rows=1, cols=2, subplot_titles=(
    "Weather Tmestamp",
    "Weather Condition"   ))

#accidents_weather_timestamp
fig.add_trace(px.bar(death_weather_timestamp, x='death_weather_timestamp', y='percentage').data[0], row=1, col=1)
#accidents_weather_condition
fig.add_trace(px.bar(death_wheather_condition, x='death_wheather_condition', y='percentage').data[0], row=1, col=2)


fig.update_layout(
    title_text="Percentage of Fatal Accidents by Wheather (%)",
    showlegend=False,
    height=600,
    width=700,
    margin=dict(l=10, r=10, t=90, b=10)  # Ajuste de margem esquerda (l) e direita (r)
)


# In[26]:


#death per road_type
death_road_type = (death_victims['road_type'].value_counts()/df['road_type'].value_counts())*100
death_road_type = death_road_type.reset_index()
death_road_type.columns = ['death_road_type', 'percentage']

#death per road_delineation
death_road_delineation = (death_victims['road_delineation'].value_counts()/df['road_delineation'].value_counts())*100
death_road_delineation = death_road_delineation.reset_index()
death_road_delineation.columns = ['death_road_delineation', 'percentage']

#death per road_direction
death_road_direction = (death_victims['road_direction'].value_counts()/df['road_direction'].value_counts())*100
death_road_direction = death_road_direction.reset_index()
death_road_direction.columns = ['death_road_direction', 'percentage']


# In[27]:


fig = sp.make_subplots(rows=2, cols=2, subplot_titles=(
    "Road Type",
    "Road Delineation",
    "Road Direction"))

#accidents_weather_timestamp
fig.add_trace(px.bar(death_road_type, x='death_road_type', y='percentage').data[0], row=1, col=1)
#accidents_road_delineation
fig.add_trace(px.bar(death_road_delineation, x='death_road_delineation', y='percentage').data[0], row=1, col=2)
#accidents_road_direction
fig.add_trace(px.bar(death_road_direction, x='death_road_direction', y='percentage').data[0], row=2, col=1)


fig.update_layout(
    title_text="Fatal Accidents by road (%)",
    showlegend=False,
    height=600,
    width=700,
    margin=dict(l=10, r=10, t=90, b=10)  # Ajuste de margem esquerda (l) e direita (r)
)


# In[28]:


#death per cause_of_accident
death_cause_of_accident = (death_victims['cause_of_accident'].value_counts()/df['cause_of_accident'].value_counts())*100
death_cause_of_accident = death_cause_of_accident.reset_index()
death_cause_of_accident.columns = ['death_cause_of_accident', 'percentage']
top10_death_cause_of_accident = death_cause_of_accident.nlargest(10,'percentage')

#death per cause_of_accident
death_type_of_accident = (death_victims['type_of_accident'].value_counts()/df['type_of_accident'].value_counts())*100
death_type_of_accident = death_type_of_accident.reset_index()
death_type_of_accident.columns = ['death_type_of_accident', 'percentage']
top10_death_type_of_accident = death_type_of_accident.nlargest(10,'percentage')


# In[29]:


fig = sp.make_subplots(rows=2, cols=2, subplot_titles=(
    "Cause of Accident",
    "Type of Accident"))

#accidents_weather_timestamp
fig.add_trace(px.bar(top10_death_cause_of_accident, x='death_cause_of_accident', y='percentage').data[0], row=1, col=1)
#accidents_road_delineation
fig.add_trace(px.bar(top10_death_type_of_accident, x='death_type_of_accident', y='percentage').data[0], row=1, col=2)

fig.update_layout(
    title_text="Fatal Accidents by Accidents (%)",
    showlegend=False,
    height=600,
    width=700,
    margin=dict(l=10, r=10, t=90, b=10)  # Ajuste de margem esquerda (l) e direita (r)
)


# In[ ]:




