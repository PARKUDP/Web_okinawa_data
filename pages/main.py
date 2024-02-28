import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import file_update as f
import culture
import hinan
import medicalcare
import AED
import os

# データ更新関数
def update_data():
    f.main("medicalcare")
    f.main("hinann")
    f.main("culture")
    f.main("Aed")

def home():
    st.title("ホーム")
    st.write("このアプリは沖縄県のデータを表示するアプリです。")
    st.write("沖縄県の魅力をより広く知ってもらうために作成しました。")
    if st.button("更新"):
        update_data()

        
# 新しいmain関数を定義
def main():
    # セッション状態変数の初期化
    if 'map_created' not in st.session_state:
        st.session_state.map_created = False

    st.sidebar.title("沖縄県のデータ")
    # サイドバーでのページ選択
    page = st.sidebar.radio(
        "ページを選択", 
        ("ホーム", "文化財", "AED", "避難", "医療機関")
    )

    if page == "ホーム":
        home()    
    elif page == "文化財":
        culture.main()
    elif page == "AED":
        AED.main()
    elif page == "避難":
        hinan.main()
    elif page == "医療機関":
        medicalcare.main()

# メイン関数の実行
if __name__ == "__main__":
    main()
