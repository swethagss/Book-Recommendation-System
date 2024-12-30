#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 22:00:03 2024

@author: swetha
"""

import pickle
import streamlit as st 
import numpy as np

st.header('Book Recommender System Using Machine Learning')
model = pickle.load(open('artifacts/model.pkl', 'rb'))
book_names = pickle.load(open('artifacts/book_names.pkl', 'rb'))
final_rating = pickle.load(open('artifacts/final_rating.pkl', 'rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))

def fetch_poster(suggestion):
    book_name = []
    poster_url = []
    
    try:
        # Get book names
        for book_id in suggestion[0]:  # Iterate over suggestions
            if book_id < len(book_pivot.index):
                book_name.append(book_pivot.index[book_id])
        
        # Match names with final_rating to get poster URLs
        for name in book_name:
            ids = np.where(final_rating['Book_Title'] == name)[0]
            if len(ids) > 0:  # If match found
                idx = ids[0]
                poster_url.append(final_rating.iloc[idx]['Image_URL_Large'])
            else:
                poster_url.append(None)  # Append None if no match found
        
        # Debugging
        st.write(f"Book Names for Posters: {book_name}")
        st.write(f"Fetched Poster URLs: {poster_url}")
        
        return poster_url
    
    except Exception as e:
        st.error(f"Error in fetch_poster: {e}")
        return []
    
def recommend_book(book_name):
    try:
        # Ensure the book exists in the pivot table
        if book_name not in book_pivot.index:
            st.error(f"Book '{book_name}' not found in book_pivot index.")
            return [], []
        
        # Get the book's index
        book_id = np.where(book_pivot.index == book_name)[0][0]
        
        # Find neighbors
        distance, suggestion = model.kneighbors(
            book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6
        )
        
        # Fetch posters
        poster_url = fetch_poster(suggestion)
        
        # Get book names
        books_list = []
        for i in range(len(suggestion[0])):  # Iterate over neighbors
            book = book_pivot.index[suggestion[0][i]]
            books_list.append(book)
        
        # Debugging
        st.write(f"Suggestions: {suggestion}")
        st.write(f"Books List: {books_list}")
        st.write(f"Poster URLs: {poster_url}")
        
        return books_list, poster_url
    
    except Exception as e:
        st.error(f"Error in recommend_book: {e}")
        return [], []
    
    
    
    
selected_books = st.selectbox(
    "Type or select a book from the dropdown",
    book_names)

if st.button('Show Recommendation'):
    recommended_books, poster_url = recommend_book(selected_books)
    st.write(f"Recommended Books: {recommended_books}")
    st.write(f"Poster URLs: {poster_url}")
    if len(recommended_books) < 6 or len(poster_url) < 6:
        st.error("Not enough recommendations or poster URLs available!")
   
    
    else:
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(recommended_books[1])
            st.image(poster_url[1])
        with col2:
            st.text(recommended_books[2])
            st.image(poster_url[2])
        with col3:
            st.text(recommended_books[3])
            st.image(poster_url[3])
        with col4:
            st.text(recommended_books[4])
            st.image(poster_url[4])
        with col5:
            st.text(recommended_books[5])
            st.image(poster_url[5])
    
    
    
    
    
    
    