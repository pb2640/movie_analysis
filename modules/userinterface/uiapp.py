"""
This file uses streamlit for a web interface to enable model deployment and serving.
"""
import pandas as pd
import streamlit as st
import plotly.express as px
import pickle
model_file = 'model_1.pkl'

st.set_page_config(
    page_title="Real-Time Movie Budget Prediction",
    page_icon="✅",
    layout="wide",
)

st.title('Real-Time Movie Budget Prediction')
st.markdown('Welcome to our real-time movie budget prediction app! You can select/change the parameters below')


@st.cache_data(persist=True)
def get_data():
    '''
    Function that returns the dataframe that contains requisite data for visualization dashboard.
    '''
    df = pd.read_csv('streamlit_data.csv')
    return df


with open(model_file, 'rb') as file:
    loaded_model = pickle.load(file)

col1, col2, col3, col4 = st.columns(4)

with col1:
    genre = st.multiselect('Select the Genre(s) you\'d like to have',['Action','Adventure','Anime'])

with col2:
    num_actors = st.number_input('Enter the number of actors you\'d like to have',step=1)

with col3:
    runtime = st.number_input('Enter the runtime (in minutes) of the movie',step=10)

with col4:
    langs = st.multiselect('Select the Language(s) you\'d like to have',['English','French','Mandarin'])



    
# create sample with data
# encode genres and languages
# pass to model for prediction