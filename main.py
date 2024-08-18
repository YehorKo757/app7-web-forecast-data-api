import streamlit as st

st.set_page_config(layout="wide")

st.title("Weather Forecast for the Next Days")
place = st.text_input(label="Place: ",
                      key="place")
days = st.slider(label="Forecast Days",
                 min_value=1,
                 max_value=5,
                 key="days",
                 help="Select the number of forecast days")
option = st.selectbox(label="Select data to view",
                      options=("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place.capitalize()}")
