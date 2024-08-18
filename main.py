import streamlit as st
import plotly.express as px
from backend import get_data

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

if place:
    try:
        data = get_data(place, days)
        dates = [dict["dt_txt"] for dict in data]

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] - 273.15 for dict in data]
            figure = px.line(x=dates,
                             y=temperatures,
                             labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            sky_conditions = [dict["weather"][0]["main"] for dict in data]
            # list comprehension or dictionary
            st.image([f"images/{condition.lower()}.png" for condition in
                      sky_conditions],
                     caption=dates,
                     width=115)

    except KeyError:
        st.error("This place is absent in the database. Please, try again.")

