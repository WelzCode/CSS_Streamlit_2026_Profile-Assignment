# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 19:38:29 2026

@author: wellz
"""
import sys; sys.path.append("..")

import streamlit as st
import pandas as pd
from logic.publication_logic import filter_by_keyword

st.title("Publications")

uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    keyword = st.text_input("Filter by keyword")
    if keyword:
        st.dataframe(filter_by_keyword(df, keyword))

    if "Year" in df.columns:
        st.subheader("Publication Trends")
        st.bar_chart(df["Year"].value_counts().sort_index())
