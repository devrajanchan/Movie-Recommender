import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommended_movies=[]
    for i in distances[1:6]:
         recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

similarity=pickle.load(open('similarity.pkl','rb'))
movie_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)
st.title("Movie Recommender")

option = st.selectbox(
    'Enter the movie on which you want recommendations',
    movies['title'].values)

if st.button('Recommend'):
    recommendation=recommend(option)
    for i in recommendation:
        st.write(i)
