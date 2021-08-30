import streamlit as st
import datetime
import requests
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="TaxiFareModel",  # => Quick reference - Streamlit
    page_icon="🚖",
    layout="centered",  # wide
)

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')
'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
'''## Please select the parameters of your ride'''
# Ask for date and time
pickup_date = st.date_input(
    'Please select a pickup date',
    datetime.date(2020, 8, 27)
)
st.write('You selected: ', pickup_date)

pickup_time = st.time_input('Select pickup time', datetime.time(8, 45))
st.write('You selected following time: ', pickup_time)

pickup_datetime = f"{pickup_date} {pickup_time}"

# Ask for pickup longitude
pickup_longitude = st.number_input(
    'Pickup longitude', value=-73.975836205698,
    step=1e-8)  #40.75308327937108, -73.975836205698
st.write('Your pickup longitude is: ', pickup_longitude)

# Ask for pickup latitude
pickup_latitude = st.number_input(
    'Pickup latitude', step=1e-8,
    value=-40.75308327937108)  # 4.854343157542917
st.write('Your pickup latitude is: ', pickup_latitude)

# Ask for dropoff longitude
dropoff_longitude = st.number_input(
    'Dropoff longitude', step=1e-8,
    value=-73.97368251324504)  #  -73.97437988130339
st.write('Your dropoff longitude is: ', dropoff_longitude)

# Ask for pickup latitude
dropoff_latitude = st.number_input(
    'Dropoff latitude', step=1e-8,
    value=40.78262576554464)  # 40.78262576554464
st.write('Your dropoff latitude is: ', dropoff_latitude)

# Ask for passenger count
passenger_count = st.number_input('Passenger count', 2)
st.write('Your passenger count is: ', passenger_count)


data = pd.DataFrame({
    'lat': [float(pickup_latitude),
            float(dropoff_latitude)],
    'lon': [float(pickup_longitude),
            float(dropoff_longitude)],
    'Taxi locations': ['Pickup', 'Dropoff'],
})

st.map(data)

'''

## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''


url = 'https://modelnew-iehtyxk3za-ew.a.run.app/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown(
        'Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...'
    )
'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
key = "2013-07-06 17:18:00.000000119"

params = {
    'key': [key],
    'pickup_datetime': [pickup_datetime],
    'pickup_longitude': [float(pickup_longitude)],
    'pickup_latitude': [float(pickup_latitude)],
    'dropoff_longitude': [float(dropoff_longitude)],
    'dropoff_latitude': [float(dropoff_latitude)],
    'passenger_count': [int(passenger_count)]
}

request = requests.get(url, params=params)

fare = request.json()['prediction']

f"You're predicted fare will be {fare}"
