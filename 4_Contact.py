# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 19:39:49 2026

@author: wellz
"""
import sys; sys.path.append("..")

import streamlit as st
from data.profile_data import PROFILE

st.title("Contact")

st.write(f"You can reach me at {PROFILE['email']}")
