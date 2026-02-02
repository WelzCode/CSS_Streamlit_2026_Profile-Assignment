# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 19:39:07 2026

@author: wellz
"""
import sys; sys.path.append("..")

import streamlit as st
from data.physics_data import physics_data
from data.astronomy_data import astronomy_data
from data.weather_data import weather_data

st.title("STEM Data Explorer")

dataset = st.selectbox(
    "Choose a dataset",
    ["Physics Experiments", "Astronomy Observations", "Weather Data"]
)

if dataset == "Physics Experiments":
    energy = st.slider("Energy (MeV)", 0.0, 10.0, (0.0, 10.0))
    st.dataframe(
        physics_data[physics_data["Energy (MeV)"].between(*energy)]
    )

elif dataset == "Astronomy Observations":
    brightness = st.slider("Brightness (Magnitude)", -15.0, 5.0, (-15.0, 5.0))
    st.dataframe(
        astronomy_data[
            astronomy_data["Brightness (Magnitude)"].between(*brightness)
        ]
    )

else:
    temp = st.slider("Temperature (°C)", -10.0, 40.0, (-10.0, 40.0))
    hum = st.slider("Humidity (%)", 0, 100, (0, 100))
    st.dataframe(
        weather_data[
            weather_data["Temperature (°C)"].between(*temp) &
            weather_data["Humidity (%)"].between(*hum)
        ]
    )
