#import folium
#import requests
#from bs4 import BeautifulSoup
# def single_map(rental_cars_location:str)->None:
#     url: str = f'https://pl.wikipedia.org/wiki/{rental_cars_location}'
#     response = requests.get(url)
#     response_html = BeautifulSoup(response.text, 'html.parser')
#     latitude = response_html.select('.latitude')[1].text.replace(",",".")
#     longitude = response_html.select('.longitude')[1].text.replace(",",".")
#     map = folium.Map(location=[latitude, longitude], zoom_start=11)
#     folium.Marker(location=[latitude, longitude],popup=f"{rental_cars_location} rządzi!!").add_to(map)
#     map.save(f'./{rental_cars_location}.html')
