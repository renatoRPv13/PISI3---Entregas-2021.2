import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import dataset.converteDataframe as dc

dc.converter()

st.set_page_config(page_title='Chessparov', page_icon='🏆')
st.title('Chessparov')
st.text('texto falando sobre o problema')

dfChess = pd.read_parquet("dataset/chess_games.parquet")
st.write(dfChess.head(10))

#ANALIZE EXPLORATORIA
graficoResult = plt.hist(x=dfChess['Result'])
plt.show()
st.pyplot(plt)
plt.hist(x=dfChess['Termination'])
st.pyplot(plt)
