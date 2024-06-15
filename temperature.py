import requests

api_key = '69527255ae9af2cefe9652be50ab3c0e'  # Replace with your actual API key
city = 'jaipur'  # Replace with the desired city name

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    # Access weather information from the 'data' dictionary
    print(f"Weather in {city}: {data['weather'][0]['description']}")
    print(f"Temperature: {data['main']['temp']}°C")
else:
    print(f"Error: {data['message']}")
