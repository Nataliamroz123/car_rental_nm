import os
import webbrowser

import folium


# import requests
# from bs4 import BeautifulSoup

def single_map(name: str, coordinates: list) -> None:
    # środek polski 52.11433, 19.42367
    map = folium.Map(location=[52.11433, 19.42367], zoom_start=7)
    for coord in coordinates:
        folium.Marker(location=[coord['latitude'], coord['longitude']], popup=f"{coord['name']}").add_to(map)
    map.save(f'./{name}.html')
    print(os.path.realpath(f'./{name}.html'))
    webbrowser.open('file://' + os.path.realpath(f'./{name}.html'))


def all_rentals_map(rental_cars: list) -> None:
    coordinates = []
    for rental in rental_cars:
        coordinates.append({
            'latitude': rental['location']['latitude'],
            'longitude': rental['location']['longitude'],
            'name': rental['name'],
        })
    single_map("all_rentals", coordinates)


def workers_map(workers: list) -> None:
    rental_name = input("Podaj nazwę wypożyczalni (brak firmy oznacza wszystkie): ")
    coordinates = []
    for worker in workers:
        if worker['workplace'] != rental_name and rental_name != "":
            continue
        coordinates.append({
            'latitude': worker['location']['latitude'],
            'longitude': worker['location']['longitude'],
            'name': f"{worker['name']} {worker['surname']}",
        })
    single_map("workers", coordinates)


def clients_map(clients: list) -> None:
    rental_name = input("Podaj nazwę wypożyczalni (brak firmy oznacza wszystkie): ")
    coordinates = []
    for client in clients:
        if client['rental'] != rental_name and rental_name != "":
            continue
        coordinates.append({
            'latitude': client['location']['latitude'],
            'longitude': client['location']['longitude'],
            'name': f"{client['name']} {client['surname']}",
        })
    single_map("clients", coordinates)
