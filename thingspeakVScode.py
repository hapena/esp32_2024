import requests

url = "https://api.thingspeak.com/update?api_key=RXKYA9KE91OV2POU"

response = requests.request("GET", url, headers=None, params="&field1= 40" + "&field2= 50" )

print(response.status_code)