import streamlit as st
import numpy as np
import pandas as pd
import datetime
import requests
# from streamlit_folium import st_folium


# st.markdown(':red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]:gray[pretty] :rainbow[colors] and :blue-background[highlight] text.')
# st.markdown(':red[Streamlit]')


############################################
# Doc : https://docs.streamlit.io/develop/api-reference/text/st.markdown
# st.markdown('''
#     :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
#     :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')


# st.markdown("TaxiFareModel UI &mdash;\
#             :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")




###########################################

# '''
# # TaxiFareModel front
# '''

# st.markdown('TaxiFare UI''''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')

# '''
# ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# '''
# # input_time = st.write('Give the date and time')
# # st.text_input("Give the date and time","var")
# date_time = st.write('Give the date')
# st.date_input("date",date_time)
# time = st.write('Give the time')
# st.time_input("time",time)

# pickup_lon = st.write('Give the pickup longitude')
# st.number_input(pickup_lon)

# pickup_lat = st.write('Give the pickup latitude')
# st.number_input(pickup_lat)

# dropoff_lon = st.write('Give the dropoff longitude')
# st.number_input(dropoff_lon)

# dropoff_lat = st.write('Give the dropoff latitude')
# st.number_input(dropoff_lat)

# passenger_count = st.write('Give the passenger count')
# st.number_input(passenger_count)



# st.image('taxi.jpg')
now = datetime.datetime.now()
# Get the date input
date_time = st.date_input("Select the date", value=now.date())
# Get the time input
time = st.time_input("Select the time", value=now.time())
## Pickup Location
pickup_lon = st.number_input("Enter the pickup longitude", value=0.0, max_value=200.00)
pickup_lat = st.number_input("Enter the pickup latitude", value=0.0, max_value=200.00)
## Dropoff Location
dropoff_lon = st.number_input("Enter the dropoff longitude", min_value=0.0, max_value=200.00)
dropoff_lat = st.number_input("Enter the dropoff latitude", min_value=0.0, max_value=200.00)
## Passenger Count
passenger_count = st.number_input("Enter the number of passengers", min_value=1, max_value=10)



params = {
    'pickup_datetime': f'{date_time} {time}',
    'pickup_longitude': pickup_lon,
    'pickup_latitude': pickup_lat,
    'dropoff_longitude': dropoff_lon,
    'dropoff_latitude': dropoff_lat,
    'passenger_count': passenger_count
}




# st.title(":taxi_de_face: Taxi Fare Predictor")
# st.markdown("""# This is the best Taxi App for Taxi Fare Prediction
# ##
# Welcome to our app:taxi: !:)""")
# st.image('taxi.jpg')



url = 'https://taxifare.lewagon.ai/predict'



# data = pd.DataFrame(dict(params))
response = requests.get(url, params=params)
# if requests.status_codes == response.raise_for_status():
if st.button('Prediction'):
    Prediction = response.json()['fare']
    st.success(f"The fare amount is '{Prediction:.2f}")
else : print("error")



# data = pd.DataFrame(dict(params))
# st.map(data)


color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", color)
