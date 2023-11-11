import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="堀 兼修 の LLC",
    layout="centered"
)

st.title('堀兼修のLLC')
st.caption('これは堀兼修のLLCです')
st.subheader('ライフラインチャート')

st.balloons()

st.snow()

df = pd.read_csv('llc/assets/csvs/llc.csv')
st.line_chart(data=df, x="年齢")

# 誕生〜幼稚園
baby_col1, baby_col2 = st.columns(2)

with baby_col1:
    st.subheader('小学校入学まで')
    st.text('幼稚園では、毎日泥団子を作って、誰が一番綺麗なまんまるで、硬くて表面はサラサラで、美しいかを競っていた気がします。')
    image = Image.open('llc/assets/images/kuchipatchi_front.png')
    st.image(image, width=200)
    
with baby_col2:
    st.line_chart(data=df.loc[0:6], x="年齢")

# 小学校
elementary_col1, elementary_col2 = st.columns(2)

with elementary_col1:
    st.subheader('小学校')
    st.text('頭悪かったです。でももしかしたら4/1生まれのせいかも。')
    image = Image.open('llc/assets/images/kuchipatchi_front.png')
    st.image(image, width=200)
    
with elementary_col2:
    st.line_chart(data=df.loc[6:12], x="年齢")

# 中学校
junior_col1, junior_col2 = st.columns(2)

with junior_col1:
    st.subheader('中学校')
    st.text('学校より塾が楽しかった。')
    image = Image.open('llc/assets/images/kuchipatchi_front.png')
    st.image(image, width=200)
    
with junior_col2:
    st.line_chart(data=df.loc[12:15], x="年齢")

# 高校
highschool_col1, highschool_col2 = st.columns(2)

with highschool_col1:
    st.subheader('高校')
    st.text('記憶ないです。')
    image = Image.open('llc/assets/images/kuchipatchi_front.png')
    st.image(image, width=200)
    
with highschool_col2:
    st.line_chart(data=df.loc[15:18], x="年齢")

# 大学
academy_col1, academy_col2 = st.columns(2)

with academy_col1:
    st.subheader('大学')
    st.text('1年目:楽しかった。2年目:単位とれねえ...3年目:もう勉強フル単。4年目:就活つらい')
    image = Image.open('llc/assets/images/kuchipatchi_front.png')
    st.image(image, width=200)
    
with academy_col2:
    st.line_chart(data=df.loc[18:22], x="年齢")

# 社会人
worker_col1, worker_col2 = st.columns(2)

with worker_col1:
    st.subheader('社会人')
    st.text('良い年と悪い年が交互にくる。')
    image = Image.open('llc/assets/images/kuchipatchi_front.png')
    st.image(image, width=200)
    
with worker_col2:
    st.line_chart(data=df.loc[23:31], x="年齢")
