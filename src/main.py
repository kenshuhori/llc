import pandas as pd
import streamlit as st
from PIL import Image

st.title('堀兼修のLLC')
st.caption('これは堀兼修のLLCです')
st.subheader('似ている有名人')
st.text('クチパッチ')

image = Image.open('llc/assets/images/kuchipatchi_front.png')
st.image(image, width=200)

st.balloons()

st.snow()

df = pd.read_csv('llc/assets/csvs/llc.csv', index_col='年齢')
st.line_chart(df)

col1, col2 = st.columns(2)

with col1:
    st.subheader('小学校入学まで')
    st.text('幼稚園では、毎日泥団子を作って、誰が一番綺麗なまんまるで、硬くて表面はサラサラで、美しいかを競っていた気がします。')
    
with col2:
    st.line_chart(df)
