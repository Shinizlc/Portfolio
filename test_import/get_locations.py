from geopy.geocoders import Yandex
from pprint import pprint

from loguru import logger
#geolocator=GoogleV3(api_key='AIzaSyAzzMjUWRIW_dJAElb2nWOMDFT2qyMcUSc')
geolocator=Yandex(api_key='7c6ca234-2db2-4ae5-9f97-b2368cca3504')
# from csv import reader
# with open('geo_loc_data.csv','r') as data:
#     for i in reader(data,delimiter=';'):
#         if i:
#             pprint(geolocator.geocode(i[0]))
#
#


pprint(geolocator.geocode('Saint Petersburg').point)