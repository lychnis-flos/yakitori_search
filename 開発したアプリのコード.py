#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import streamlit as st
import plotly.express as px


# In[2]:


# 整形・加工後のデータ.csvを読み込む
merged_df=pd.read_csv("整形・加工後のデータ.csv")


# In[3]:


# streamlistの部品設計
st.title("サロンサーチ")

#　フィルタ設定
price_limit=st.slider("最低価格の上限",min_value=1000,max_value=10000,step=200,value=6000)
score_limit=st.slider("人気スコアの下限",min_value=0.0,max_value=20.0,step=1.0,value=5.0)


# In[5]:


#　フィルタ修理
filtered_df = merged_df[
    (merged_df['price'] <= price_limit)&
    (merged_df['pop_score'] >= score_limit)
]


# In[7]:


#　散歩図の作成(人気スコア * 最低カット価格)
fig = px.scatter(
filtered_df,
x='pop_score',
y='price',
hover_data=['name_data', 'access','star', 'review'],
title='人気スコアと最低カット価格の散布図'
)
st.plotly_chart(fig)


# In[8]:


selected_data = st.selectbox('気になるサロンを選んで詳細を確認', filtered_df['name_data'])

if selected_data:
    url = filtered_df[filtered_df['name_data'] == selected_data]['link_detail'].values[0]
    st.markdown(f"[{selected_data}のページへ移動]({url})", unsafe_allow_html=True)


# In[9]:


sort_key = st.selectbox(
    "ランキング基準を選んでください",
    ("star", "pop_score", "review", "price")
)

ascending = True if sort_key == "price" else False


# In[10]:


st.subheader(f"{sort_key} によるサロンランキング（上位10件）")

ranking_df = filtered_df.sort_values(by=sort_key, ascending=ascending).head(10)

st.dataframe(ranking_df[["name_data", "price", "pop_score", "star", "review", "access"]])


# In[ ]:





# In[ ]:




