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


col1, col2, col3, col4, col5, col6= st.columns(6)

with col1:
    genres_list =  ['Action', 'Adult', 'Adventure', 'Animation', 'Biography', 'Comedy',
                    'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Film-Noir',
                    'Game-Show', 'History', 'Horror', 'Music', 'Musical', 'Mystery',
                    'News', 'Reality-TV', 'Romance', 'Sci-Fi', 'Short', 'Sport',
                    'Talk-Show', 'Thriller', 'War', 'Western']
    genre = st.multiselect('Select the Genre(s) you\'d like to have', genres_list)

with col2:
    num_actors = st.number_input('Enter the number of actors',step=1, value=10)

with col3:
    runtime = st.number_input('Enter the movie runtime (in minutes)',step=10, value=90)

with col4:
    common_langs = ['English','French','Spanish','German','Arabic','Hindi','Italian','Chinese','Mandarin','Russian', 'Latin', 'Japanese', 'Persian', 'Bengali']
    langs = st.multiselect('Select the Language(s)',common_langs)
    

with col5:
    release_year = st.number_input('Select the release year of the movie', min_value=2022, max_value=2030)
    release_year = int(release_year)
    

with col6:
    company_list = ['Amblin Entertainment', 'American Film Institute (AFI)',
                    'Bigfott Studios', 'Blumhouse Productions', 'BondIt Media Capital',
                    'Columbia Pictures', 'Cyfuno Ventures', 'El Dorado Films',
                    'Entertain Me Productions', 'JC Films', 'Mattioli Productions',
                    'Metro-Goldwyn-Mayer (MGM)', 'North Bank Entertainment', 'Others',
                    'Paramount Pictures', 'Reality Entertainment (RE)',
                    'Small Town Monsters.', 'Twentieth Century Fox', 'Universal Pictures',
                    'University of Southern California, School of Cinematic Arts',
                    'Veteran Documentary Corps', 'Walt Disney Pictures', 'Warner Bros.',
                    'Weston Woods Studios']

    prod_company = st.multiselect('Select the production company', company_list)


user_input = dict()
user_input['runtime'] = runtime
user_input['num_actors'] = num_actors
user_input['release_year'] = release_year
for i in genre:
    user_input[i] = 1
for i in langs:
    user_input[i] = 1
for i in prod_company:
    user_input[i] = 1


input_df = pd.DataFrame(columns=['num_actors', 'runtime', 'Action', 'Adult', 'Adventure', 'Animation', 'Biography', 'Comedy',
        'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Film-Noir', 'Game-Show', 'History', 'Horror', 'Music', 'Musical',
        'Mystery', 'News', 'Reality-TV', 'Romance', 'Sci-Fi', 'Short', 'Sport', 'Talk-Show', 'Thriller', 'War', 'Western', 'Arabic',
        'Bengali', 'Chinese', 'English', 'French', 'German', 'Hindi', 'Italian', 'Japanese', 'Mandarin', 'Persian', 'Russian', 'Spanish',
        'Amblin Entertainment', 'American Film Institute (AFI)', 'Bigfott Studios', 'Blumhouse Productions', 'BondIt Media Capital', 'Columbia Pictures',
        'Cyfuno Ventures', 'El Dorado Films', 'Entertain Me Productions', 'JC Films', 'Mattioli Productions', 'Metro-Goldwyn-Mayer (MGM)', 'North Bank Entertainment',
        'Others', 'Paramount Pictures', 'Reality Entertainment (RE)', 'Small Town Monsters.', 'Twentieth Century Fox', 'Universal Pictures', 'University of Southern California, School of Cinematic Arts',
        'Veteran Documentary Corps', 'Walt Disney Pictures', 'Warner Bros.', 'Weston Woods Studios', 'release_year'])

input_df.loc[len(input_df)] = user_input
input_df = input_df.fillna(0)
# input_df['num_actors'] = input_df['num_actors'].astype('int')
# input_df['runtime'] = input_df['runtime'].astype('int')
# input_df['release_year'] = input_df['release_year'].astype('int')


if st.button('Predict'):
    if not (genre and langs and prod_company):
        st.error('Kindly make sure all selections have been made!', icon="🚨")
    else:
        val = round(loaded_model.predict(input_df)[0])
        if val>0:
            st.markdown(f'The estimated budget of your movie is **${val:,}**.')
        else:
            st.markdown(f'The estimated budget of your movie is **$1,422,607**.')
    
