import requests

url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q": "51.1,-0.13"}

headers = {
    "X-RapidAPI-Key": "ecd00f4671msh30a13305959bd93p191dc7jsnf419a745b1ca",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

if response.status_code == 200:
    data = response.json()
    print("Weather Data:")
    print(data)
else:
    print("Failed to retrieve weather data. Status code:", response.status_code)
