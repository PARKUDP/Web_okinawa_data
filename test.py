import streamlit as st

# 各ページの内容を定義する関数
def page1():
    st.title("ページ1")
    st.write("これはページ1です。")

def page2():
    st.title("ページ2")
    st.write("これはページ2です。")

def page3():
    st.title("ページ3")
    st.write("これはページ3です。")

# メイン関数
def main():
    st.sidebar.title("ナビゲーション")
    # サイドバーでページ選択
    page = st.sidebar.radio("ページを選択", ("ページ1", "ページ2", "ページ3"))

    # 選択されたページに応じて関数を呼び出す
    if page == "ページ1":
        page1()
    elif page == "ページ2":
        page2()
    elif page == "ページ3":
        page3()

if __name__ == "__main__":
    main()
