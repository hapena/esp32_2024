import requests

url = "https://deckofcardsapi.com/api/deck/new/shuffle/"

response = requests.request("GET", url, headers=None, params="deck_count:1")
print(response.status_code)
print(response.text)
deck = response.json()
deck_id = deck['deck_id']
print(deck_id)
