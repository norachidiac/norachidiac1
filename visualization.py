import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import plotly.graph_objects as go
from plotly.offline import iplot
import plotly as plt
import plotly.express as px
import chart_studio.plotly as py
import plotly.offline as py  
st.title('Leading Cause of Death: Covid-19')
from asyncore import write
df = pd.read_csv("/Users/noura/Desktop/Death Causes.csv")
st.write("In our lives, many viruses and diseases have emerged that have led to an increase in death rates. This application provides information about the leading cause of deaths particularly an emerging one:") 
st.write("Covid-19") 
st.image("https://www.who.int/images/default-source/mca/mca-covid-19/coronavirus-2.tmb-1920v.jpg?Culture=en&sfvrsn=4dba955c_6.jpg")
def load_data(nrows):
    data = pd.read_csv("/Users/noura/Desktop/Death Causes.csv", nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

table = ff.create_table(data)
if st.checkbox('Show Table'):
    st.subheader('Table')
    st.write(table)
df = pd.read_csv("/Users/noura/Desktop/drug_deaths.csv")
df1= [go.Bar (x=df.Location, y=df.Heroin)]
py.offline.init_notebook_mode(connected=True)

import plotly.graph_objs as go
from plotly.figure_factory import create_table
py.offline.iplot(df1)
if st.checkbox('Show Barplot Drug Deaths'):
    st.subheader('Plotting Inline')
    st.write(df1)

from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim
import geopy
import geocoder
longitude = []
latitude = []
df_covid = pd.read_csv("/Users/noura/Desktop/covid2.csv")
fig = px.density_mapbox(df_covid, lat = "HighestInfectionCount", lon ="PercentPopulationInfected", z = "Population", radius = 10, 
                       center = dict(lat = 9, lon =8), zoom = 1, hover_name = 'Location', 
                       mapbox_style = 'open-street-map', title = 'Covid Infections')
if st.checkbox('Show Mapbox'):
    st.subheader('Highest Covid Infections')
    st.write(fig)

px = px.scatter(df_covid, x = "Location", y = "HighestInfectionCount")
if st.checkbox('Show Scatter Plot'):
    st.subheader('Scatter Plot')
    st.write(px)

s = np.linspace(0, 2 * np.pi, 240)
t = np.linspace(0, np.pi, 240)
tGrid, sGrid = np.meshgrid(s, t)
r = 2 + np.sin(7 * sGrid + 5 * tGrid) 
x = r * np.cos(sGrid) * np.sin(tGrid) 
y = r * np.sin(sGrid) * np.sin(tGrid)  
z = r * np.cos(tGrid) 
surface = go.Surface(x=x, y=y, z=z)
data3 = [surface]
layout = go.Layout(
    title='Parametric Plot',
    scene=dict(
        xaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        yaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        zaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        )
    )
)

fig2 = go.Figure(data=data3, layout=layout)
py.iplot(fig2)
if st.checkbox('Show Parametric Plot'):
    st.subheader('Parametric Plot')
    st.write(fig2)
    

