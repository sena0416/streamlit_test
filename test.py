import streamlit as st
import pandas as pd
import datetime

#Hello Worldを表示する
st.write("Hello World")
#Hello Worldを表示する（後半文字色変更）
st.write("Hello :blue[World]")
#Hello Worldを表示する（タイトル)
st.title("Hello World")
#Hello Worldを表示する（着物アイコンだす）
st.title("Hello World :kimono:")
#データフレームを表示する
st.write(
    pd.DataFrame(
        {
            "first column":[1,2,3,4],
            "second column":[5,6,7,8]
        }
    )
)
#URLのリンクボタンを表示する
st.link_button("Click here","https://www.tableau.com/ja-jp/community/public")
#ヘッダーを表示する（ヘッダーの下に虹を書く)
st.header("Hello World",divider="rainbow")
#コードを表示する（超便利そう）
code = """print("hello")"""
st.code(code,language="python")
#チェックボックスを作成する
agree = st.checkbox("I agree")
#もし、チェックボックスを押したらOkと表示する
if agree:
    st.write("OK!")
#マルチセレクト
options = st.multiselect(
    "好きな色は何ですか？",
    ["赤","緑","青","黄色"]
)
st.write("あなたの選んだ色は:",options)
#シングルセレクト
options = st.radio(
    "好きな色は何ですか？",
    ["赤","緑","青","黄色"]
)
st.write("あなたの選んだ色は:",options)
#修正できるデータフレーム
df = pd.DataFrame(
    [
        {"colors":"赤","rating":4},
        {"colors":"緑","rating":5},
        {"colors":"青","rating":3}
    ]
)
edited_df = st.data_editor(df)
#最も高い点数を表示する(ページ内で記載弄ってもしっかり反映してくれる)
st.write("最も点数が高い色は:",edited_df.iloc[edited_df["rating"].idxmax()]["colors"])
st.write("一番点数が高いのは:",edited_df["rating"].max())
#修正できるデータフレーム(応用版)
df = pd.DataFrame(
    [
        {"colors":"赤","rating":4,"mark":True},
        {"colors":"緑","rating":5,"mark":True},
        {"colors":"青","rating":3,"mark":True}
    ]
)
edited_df = st.data_editor(df)
edited_df2 = edited_df[edited_df["mark"]==True]
#最も高い点数を表示する(ページ内で記載弄ってもしっかり反映してくれる)
st.write("最も点数が高い色は:",
         edited_df2.loc[edited_df2["rating"].idxmax()]["colors"])
#ダウンロードボタンを作成する
csv_df = edited_df2.to_csv().encode("shift-jis")
st.download_button(
    label = "CSVをダウンロード",
    data = csv_df,
    file_name = 'sample_data.csv',
    mime = "text/csv"
)

#プログレスバーを表示
df = pd.DataFrame(
    {
        "sales":[20,55,100,80],
        "progress_sales":[20,55,100,80]
    }
)

st.data_editor(
    df,
    column_config = {
        "progress_sales":st.column_config.ProgressColumn(
            min_value=0,
            max_value=100
        ),
    },
)
#時系列表示
df = pd.DataFrame(
    {
        "sales":[
            [0,4,26],
            [3,50,0],
            [i for i in range(100)]
        ]
    }
)
st.data_editor(
    df,
    column_config={
        "sales": st.column_config.BarChartColumn(
            y_min=0,
            y_max=100
        )

    }
)
#時系列折れ線ぐふ
st.data_editor(
    df,
    column_config={
        "sales": st.column_config.LineChartColumn(
            y_min=0,
            y_max=100
        )

    }
)
#ユーザのインプット表示(スライダー)
age = st.slider("あなたは何歳ですか？",0,130,40)
st.write("私は",age,"歳です")
#日付選択
date = st.date_input("あなたが生まれたのはいつですか？",datetime.date(1993,4,16))
st.write("私は",date,"に生まれました。")
#ユーザの自由記述
text = st.text_input("入力してください","xxxxxxxxxxx")
st.write(text)
#カラムを分ける方法
col1,col2,col3 = st.columns(3)
with col1:
    st.title("column1")
    st.write("これはカラムの1です。")
with col2:
    st.title("column2")
    st.write("これはカラムの2です。")
with col3:
    st.title("column3")
    st.write("これはカラムの3です。")
#タブを分ける
tab1,tab2 = st.tabs(["tab1","tab2"])
with tab1:
    st.title("tab1")
    st.write("これはタブの1です。")
with tab2:
    st.title("tab2")
    st.write("これはタブの2です。")
#アコーディオン表示をする
with st.expander("もっと詳しく見る"):
    st.write("くわしい")
#ポップアップ表示
with st.popover("もっと詳しく見る"):
    st.write("XXXXXXXX")
#サイドバー
with st.sidebar:
    st.write("AAAAAA")
    st.write("nnnnnnn")
#nortification
agree = st.checkbox("同意しますか？")
if agree:
    st.toast("Thank you",icon="👍")
birthday = st.checkbox("本日はあなたの誕生日ですか？")
if birthday:
    st.toast("おめでとうございます！")
    st.balloons()
#複数ページ実装(外部リンクを挿入することも当然可能)
st.page_link("test.py",label="Home",icon="🏠")
st.page_link("pages/page1.py",label="Page1")
st.page_link("pages/page2.py",label="Page2")

