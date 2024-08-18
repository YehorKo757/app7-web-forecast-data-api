import os
import requests


def get_data(place, forecast_days=None):
    # use st.secrets() instead of os.getenv() while deploying to streamlit
    url = (f"https://api.openweathermap.org/data/2.5/forecast?"
           f"q={place}&"
           f"appid={os.getenv("OpenWeatherApi")}")
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    number_of_values = 8 * forecast_days
    filtered_data = filtered_data[:number_of_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo"))
