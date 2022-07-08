import streamlit as st
import pandas as pd

st.set_page_config(page_title='Chessparov', page_icon='🏆')
st.title('Chessparov')
st.text('texto falando sobre o problema')
df = pd.read_csv("dataset/chess_games.csv")
st.write(df)

