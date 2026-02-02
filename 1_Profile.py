# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 19:38:02 2026

@author: wellz
"""
import sys
sys.path.append("..")
from pathlib import Path
import os
import streamlit as st
from data.profile_data import PROFILE

st.title("Profile")

with st.container():
    st.subheader(PROFILE["name"])
    st.caption(PROFILE["title"])
    current_dir = os.path.dirname(__file__)
    image_path = os.path.join(current_dir, "..", "assets", "profile.jpg")
    st.image(image_path, width=160)
    st.write(PROFILE["bio"])

st.divider()

with st.container():
    st.subheader("Skills")
    cols = st.columns(2)
    for i, skill in enumerate(PROFILE["skills"]):
        cols[i % 2].write(f"- {skill}")

st.divider()

with st.container():
    st.subheader("Projects")
    for project in PROFILE["projects"]:
        st.write(f"- {project}")

st.divider()

with st.container():
    st.subheader("Contact")
    st.write(PROFILE["email"])

    cv_path = Path("assets/Welcome_Chirwa_CV.pdf")
    with open(cv_path, "rb") as file:
        st.download_button(
            label="📄 Download CV",
            data=file,
            file_name="Welcome_Chirwa_CV.pdf",
            mime="application/pdf"
        )
