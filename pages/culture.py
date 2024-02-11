import streamlit as st
import urllib.request as urllib2
import json
import pandas as pd
import folium
from streamlit_folium import st_folium
import file_update as f
import os
current_dir = os.path.dirname(__file__)
culture_path = os.path.join(current_dir, 'data','culture.csv')

# データ更新関数
def update_data():
    f.main("culture")
    
# データ取得関数
def get_data():
    df = pd.read_csv(culture_path)
    df = df.dropna(subset=['緯度', '経度'])
    return df

# 文化財をテーブルで表示する関数
def table():
    st.title("文化財一覧（テーブル）")
    st.button("更新", on_click=update_data)
    data = get_data()
    filter_input = st.text_input("地域").lower()
    if filter_input:
        # NaN値を含まない行に対してフィルタリングを行う
        data = data[data['住所'].str.lower().fillna('').str.contains(filter_input)]
    st.dataframe(data[['名称', '住所', '緯度', '経度']], 1000, 450)


# 地図を表示する関数
def show_map(data):
    n = folium.Map(location=[26.212401, 127.680932], zoom_start=6)
    
    for i, row in data.iterrows():
        folium.Marker([row['緯度'], row['経度']], popup=row['名称']).add_to(n)
    st_data = st_folium(n, width=720, height=480)

# 文化財を地図で表示する関数
def map():
    st.title("文化財（地図）")
    if st.button("更新"):
        update_data()
        st.session_state.map_created = False

    data = get_data()
    filter_input = st.text_input("地域").lower()
    if filter_input:
        # NaN値を含まない行に対してフィルタリングを行う
        data = data[data['住所'].str.lower().fillna('').str.contains(filter_input)]

    if st.button("地図を表示"):
        st.session_state.map_created = True

    if st.button("地図非表示"):
        st.session_state.map_created = False
        
    if st.session_state.map_created:
        show_map(data)

def tool():
    st.title("地域分析")
    st.write("ここでは、地域分析を行います。")
    st.write("地域分析には、以下の機能があります。")
    data = get_data()
    st.write("・地域の文化財の数を表示")
    st.write("・地域の文化財の数を地図で表示")
    st.write("・地域の文化財の数をグラフで表示")
    st.write("・地域の文化財の数を表で表示")
    st.write("・地域の文化財の数をCSVで出力")
# Streamlitアプリのメイン関数
def main():
    st.sidebar.title("文化財")
    
    page = st.sidebar.radio("ページを選択", ("文化財一覧（テーブル）", "文化財一覧（地図）"))
    
    if page == "文化財一覧（テーブル）":
        table()
    elif page == "文化財一覧（地図）":
        map()
    elif page == "地域分析":
        tool()

# メイン関数の実行
if __name__ == "__main__":
    if 'map_created' not in st.session_state:
        st.session_state.map_created = False  # セッション状態の初期化
    main()