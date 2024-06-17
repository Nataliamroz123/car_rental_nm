#import folium
#import requests
#from bs4 import BeautifulSoup

# def single_map(location: tuple) -> None:
#     url: str = f'https://pl.wikipedia.org/wiki/{location[0]}'
#     response = requests.get(url)
#     response_html = BeautifulSoup(response.text, 'html.parser')
#     latitude = response_html.select('.latitude')[1].text.replace(",", ".")
#     longitude = response_html.select('.longitude')[1].text.replace(",", ".")
#     map = folium.Map(location=[latitude, longitude], zoom_start=11)
#     folium.Marker(location=[latitude, longitude], popup=f"{location[0]} rządzi!!").add_to(map)
#     map.save(f'./{location[0]}.html')

def all_rentals_map() -> None:
    locations = [(rental['name'], rental['location']) for rental in rental_cars]
    map = folium.Map(location=[50.0641924, 19.9449744], zoom_start=6)
    for location in locations:
        folium.Marker(location=[location[1]['latitude'], location[1]['longitude']], popup=location[0]).add_to(map)
    map.save('all_rentals.html')

def workers_map(worker_list: list) -> None:
    locations = [(worker['name'], worker['surname'], worker['location']) for worker in worker_list]
    map = folium.Map(location=[50.0641924, 19.9449744], zoom_start=6)
    for location in locations:
        folium.Marker(location=[location[2]['latitude'], location[2]['longitude']], popup=f"{location[0]} {location[1]}").add_to(map)
    map.save(f'workers_map.html')

def clients_map(client_list: list) -> None:
    locations = [(client['name'], client['surname'], client['location']) for client in client_list]
    map = folium.Map(location=[50.0641924, 19.9449744], zoom_start=6)
    for location in locations:
        folium.Marker(location=[location[2]['latitude'], location[2]['longitude']], popup=f"{location[0]} {location[1]}").add_to(map)
    map.save(f'clients_map.html')

#def rental_workers_map(worker_list: list) -> None: