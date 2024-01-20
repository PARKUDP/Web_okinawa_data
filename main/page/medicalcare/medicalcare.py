import streamlit as st
import urllib.request as urllib2
import json
import pandas as pd
import folium
from streamlit_folium import st_folium
#from .. import data as d

def update_data():
    d.main("medicalcare")
    
def get_data():
    df = pd.read_csv("../data/medicalcare.csv")
    return df

# Streamlitアプリのメイン関数
def table():
    st.title("医療機関一覧（テーブル）")
    #st.button("更新", on_click=update_data)
    data = get_data()
    filter_input = st.text_input("フィルタ").lower()
    if filter_input:
        data = data[data['名称'].str.lower().str.contains(filter_input)]

    st.dataframe(data[['名称', '住所', '緯度', '経度']], 1000, 450)

def map():
    st.title("医療機関一覧（地図）")
    #st.button("更新", on_click=update_data)
    data = get_data()
    filter_input = st.text_input("フィルタ").lower()
    if filter_input:
        data = data[data['名称'].str.lower().str.contains(filter_input)]
    
    n = folium.Map(location=[26.212401, 127.680932], zoom_start=6)
    
    for i, row in data.iterrows():
        folium.Marker([row['緯度'], row['経度']], popup=row['名称']).add_to(n)
    st_data = st_folium(n)
    
def main():
    st.sidebar.title("医療")
    
    page = st.sidebar.radio("ページを選択", ("医療機関一覧（テーブル）", "医療機関一覧（地図）"))
    
    if page == "医療機関一覧（テーブル）":
        table()
    elif page == "医療機関一覧（地図）":
        map()
        
if __name__ == "__main__":
    main()