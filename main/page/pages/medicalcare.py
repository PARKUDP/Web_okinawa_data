import streamlit as st
import urllib.request as urllib2
import json
import pandas as pd
import folium
from streamlit_folium import st_folium
import file_update as f

# データ更新関数
def update_data():
    f.main("medicalcare")
    
# データ取得関数
def get_data():
    df = pd.read_csv("../data/medicalcare.csv")
    return df

# 医療機関をテーブルで表示する関数
def table():
    st.title("医療機関一覧（テーブル）")
    st.button("更新", on_click=update_data)
    data = get_data()
    filter_input = st.text_input("地域").lower()
    if filter_input:
        data = data[data['住所'].str.lower().str.contains(filter_input)]

    st.dataframe(data[['名称', '住所', '緯度', '経度']], 1000, 450)

# 地図を表示する関数
def show_map(data):
    n = folium.Map(location=[26.212401, 127.680932], zoom_start=6)
    
    for i, row in data.iterrows():
        folium.Marker([row['緯度'], row['経度']], popup=row['名称']).add_to(n)
    st_data = st_folium(n, width=720, height=480)

# 医療機関を地図で表示する関数
def map():
    st.title("医療機関一覧（地図）")
    if st.button("更新"):
        update_data()
        st.session_state.map_created = False  # 更新ボタンが押されたら地図の表示をリセット

    data = get_data()
    filter_input = st.text_input("地域").lower()
    if filter_input:
        data = data[data['住所'].str.lower().str.contains(filter_input)]

    if st.button("地図を表示"):
        st.session_state.map_created = True  # 地図表示ボタンが押されたら状態を更新

    if st.button("地図非表示"):
        st.session_state.map_created = False  # 地図非表示ボタンが押されたら状態を更新  
        
    if st.session_state.map_created:
        show_map(data)  # 地図を表示

# Streamlitアプリのメイン関数
def main():
    st.sidebar.title("医療")
    
    page = st.sidebar.radio("ページを選択", ("医療機関一覧（テーブル）", "医療機関一覧（地図）"))
    
    if page == "医療機関一覧（テーブル）":
        table()
    elif page == "医療機関一覧（地図）":
        map()

# メイン関数の実行
if __name__ == "__main__":
    if 'map_created' not in st.session_state:
        st.session_state.map_created = False  # セッション状態の初期化
    main()