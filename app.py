import streamlit as st
import pandas as pd
import numpy as np
import base64
from io import BytesIO

st.set_page_config(page_title="Welcome Chirwa - Application Developer", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to:",
    ["Profile", "Publications", "STEM Data Explorer", "Contact"]
)

physics_data = pd.DataFrame({
    "Experiment": ["Alpha Decay", "Beta Decay", "Gamma Ray Analysis", "Quark Study", "Higgs Boson"],
    "Energy (MeV)": [4.2, 1.5, 2.9, 3.4, 7.1],
    "Date": pd.date_range(start="2024-01-01", periods=5),
})

astronomy_data = pd.DataFrame({
    "Celestial Object": ["Mars", "Venus", "Jupiter", "Saturn", "Moon"],
    "Brightness (Magnitude)": [-2.0, -4.6, -1.8, 0.2, -12.7],
    "Observation Date": pd.date_range(start="2024-01-01", periods=5),
})

weather_data = pd.DataFrame({
    "City": ["Cape Town", "London", "New York", "Tokyo", "Sydney"],
    "Temperature (°C)": [25, 10, -3, 15, 30],
    "Humidity (%)": [65, 70, 55, 80, 50],
    "Recorded Date": pd.date_range(start="2024-01-01", periods=5),
})

PROFILE = {
    "name": "Welcome Chirwa",
    "title": "Application Developer",
    "bio": "Completed a Diploma in Application Development and currently expanding skills in data analysis and data-driven systems.",
    "skills": ["Python", "Streamlit", "PHP", "MySQL", "HTML", "JavaScript", "C++", "Java", "Kotlin", "XAMPP"],
    "projects": ["Clinic Management System"],
    "email": "wellzchirwa22@gmail.com"
}

# ---------------- Embedded image and PDF ----------------
# Replace these base64 strings with your own converted files
IMG_B64 = "..."  # base64 string of profile image
PDF_B64 = "..."  # base64 string of CV PDF

img_bytes = base64.b64decode(IMG_B64)
pdf_bytes = base64.b64decode(PDF_B64)

# ---------------- PAGE LOGIC ----------------
if page == "Profile":
    st.title("Profile")
    with st.container():
        st.subheader(PROFILE["name"])
        st.caption(PROFILE["title"])
        st.image(img_bytes, width=160)
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

if page == "Publications":
    st.title("Publications")
    uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)
        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            filtered = publications[
                publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
            ]
            st.write(f"Filtered Results for '{keyword}':")
            st.dataframe(filtered)
        else:
            st.write("Showing all publications")
        if "Year" in publications.columns:
            st.subheader("Publication Trends")
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)
        else:
            st.write("The CSV does not have a 'Year' column to visualize trends.")

if page == "STEM Data Explorer":
    st.title("STEM Data Explorer")
    data_option = st.selectbox(
        "Choose a dataset to explore",
        ["Physics Experiments", "Astronomy Observations", "Weather Data"]
    )
    if data_option == "Physics Experiments":
        st.write("### Physics Experiment Data")
        st.dataframe(physics_data)
        energy_filter = st.slider("Filter by Energy (MeV)", 0.0, 10.0, (0.0, 10.0))
        filtered_physics = physics_data[
            physics_data["Energy (MeV)"].between(energy_filter[0], energy_filter[1])
        ]
        st.write(f"Filtered Results for Energy Range {energy_filter}:")
        st.dataframe(filtered_physics)
    elif data_option == "Astronomy Observations":
        st.write("### Astronomy Observation Data")
        st.dataframe(astronomy_data)
        brightness_filter = st.slider("Filter by Brightness (Magnitude)", -15.0, 5.0, (-15.0, 5.0))
        filtered_astronomy = astronomy_data[
            astronomy_data["Brightness (Magnitude)"].between(brightness_filter[0], brightness_filter[1])
        ]
        st.write(f"Filtered Results for Brightness Range {brightness_filter}:")
        st.dataframe(filtered_astronomy)
    elif data_option == "Weather Data":
        st.write("### Weather Data")
        st.dataframe(weather_data)
        temp_filter = st.slider("Filter by Temperature (°C)", -10.0, 40.0, (-10.0, 40.0))
        humidity_filter = st.slider("Filter by Humidity (%)", 0, 100, (0, 100))
        filtered_weather = weather_data[
            weather_data["Temperature (°C)"].between(temp_filter[0], temp_filter[1]) &
            weather_data["Humidity (%)"].between(humidity_filter[0], humidity_filter[1])
        ]
        st.write(f"Filtered Results for Temperature {temp_filter} and Humidity {humidity_filter}:")
        st.dataframe(filtered_weather)

if page == "Contact":
    st.title("Contact")
    st.write(PROFILE["email"])
    st.download_button(
        label="📄 Download CV",
        data=BytesIO(pdf_bytes),
        file_name="Welcome_Chirwa_CV.pdf",
        mime="application/pdf"
    )
