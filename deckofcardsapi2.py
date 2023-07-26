import requests

url = "https://deckofcardsapi.com/api/deck/s5tzlk5khece/draw/"


response = requests.request("GET", url, headers=None, params="count=3")
print(response.status_code)

deck = response.json()
print(deck)
