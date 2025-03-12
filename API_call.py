import requests
url = "https://shorturl.at/onbGO"
response = requests.post(url)
if response.status_code == 200:
    print("Data sent successfully!")
    print("Response:", response.json())
else:
    print("Failed to send data. Status Code:", response.status_code)