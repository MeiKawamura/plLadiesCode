import streamlit as st
import pandas as pd

st.title('私のデータ分析アプリ')
st.text('データ分析してみた！')
st.markdown('## これは項目名')
st.markdown('- これは項目の説明です')
st.markdown('- どうもどうも:bow:')

df = pd.DataFrame({
    'A列': [1, 2, 3, 4],
    'B列': [10, 20, 40, 30],
    'C列': [400, 100, 200, 300],
})

# st.writeを使ったDataFrameの表示
st.write(df)

# st.dataframeを使ったDataFrameの表示 (列の最大値をハイライトし、表示サイズを指定しています)
st.dataframe(df.style.highlight_max(axis=0), width=500, height=200)

st.markdown('行列変えたければ:star:')
# st.dataframeを使ったDataFrameの表示 (列の最大値をハイライトし、表示サイズを指定しています)
st.dataframe(df.style.highlight_max(axis=1), width=500, height=200)

st.subheader("PyLadies Tokyo 参加者推移")

data = [
    [15,22,5],
    [5,15,12],
    [41,40,21],
    [19,13,0],
    [23,27,0],
    [17,21,7],
    [28,8,8],
    [6,8,13],
    [7,10,20],
    [35,20,18],
    [13,9,8],
    [21,4,32],
]

months = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
chart_data = pd.DataFrame(
    data,
    columns=['2015', '2020', '2023'],
    index=pd.CategoricalIndex(months, categories=months, ordered=True)
)

st.line_chart(chart_data)
st.area_chart(chart_data)
st.bar_chart(chart_data)

st.image('/Users/kawamura.co.jp/Desktop/cist3au/pyLadies/images/hiro_cat.JPG', caption='猫', use_column_width=True)

name = st.text_input('名前を入力してください')
st.write('名前:', name)

agree = st.checkbox('画像を表示しますか？')
if agree:
    st.image('/Users/kawamura.co.jp/Desktop/cist3au/pyLadies/images/decakiyo.jpg', caption='キュイーン', use_column_width=False)

agree = st.checkbox('本当に？')
if agree:
    st.image('images/yamakawat.jpg', caption='キュイーン', use_column_width=False)
    st.balloons()

options = st.multiselect(
    'あなたの好きな色を選んでください',
    options=['青', '黄色', '赤', 'ピンク', '金色'],
    default=['青'],
)
st.write('好きな色:', options)

history = st.slider("Python歴は?", 0, 33, 3)
st.write("私のPython歴は ", history, "です")

picture = st.camera_input("撮影!")
if picture:
    st.image(picture)

uploaded_file = st.file_uploader('画像を選択してください', type=['jpg','png'])
if uploaded_file is not None:
    st.image(uploaded_file)

uploaded_csv_file = st.file_uploader('csvファイルを選択してください', type=['csv'])
if uploaded_csv_file is not None:
    csv_df = pd.read_csv(uploaded_csv_file)
    st.write(df)

st.sidebar.markdown('[google](https://google.com)')

# import datetime

# name = 'MeiKawamura'
# today = datetime.date.today()
# next_birth = datetime.date(2025,1,16)

# cnt = (next_birth - today).days

# if cnt<90:
#     st.markdown('３ヶ月以内に誕生日ですね！わーい！')
#     st.balloons()
# elif cnt>270:
#     st.markdown('まだまだ先だね！誕生日から3ヶ月経ってないすね！')
# else :
#     st.markdown('なんでもない日におめでとう')