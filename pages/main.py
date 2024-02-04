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
    st.title("沖縄県のデータ分析")
    st.write("ここでは、沖縄県のデータを分析しています。現在のところでは、データが不足しているため、避難場所、医療機関、文化財、AEDのデータを分析しています。（ちなみにデータが足りない場合も存在します。）")
    if st.button("更新"):
        update_data()
    current_dir = os.path.dirname(__file__)
    image_path = os.path.join(current_dir, 'image', 'image.png')
    st.image(image_path, caption='image')

        
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
