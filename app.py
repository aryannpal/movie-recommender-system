import streamlit as st
import pickle

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


movies=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')
selected_movies_names= st.selectbox(
    "Search for the Movies",
    movies['title'].values)
if st.button("Recommend"):
    recommendation=recommend(selected_movies_names)
    for i in recommendation:
        st.write(i)


