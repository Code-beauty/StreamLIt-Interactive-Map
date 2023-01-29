import streamlit as st
from shapely.geometry import Point, Polygon
import geopandas as gpd
import pandas as pd
import geopy

from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

street = st.sidebar.text_input("Street"," ")
city = st.sidebar.text_input("City","SD")
province = st.sidebar.text_input("Province","SD")
country = st.sidebar.text_input("Country".,"United States")

geolocator = Nominatim(user_agent="GTA Lookup")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
location = geolocator.geocode(street+", "+city+", "+province+", "+country)


st.header(street)
lat = location.latitude
lon = location.longitude
map_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})
st.map(map_data , zoom = 12) 




