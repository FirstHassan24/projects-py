import requests
# Store your API key
WEATHER_API_KEY = "d028fe121ba24396b61141747250807"
#TODO:Hit weather api's forecast endpoint for 7 days of data. Display it in an easy-to-read and useful way in the console (date + day of week, temperature, and a word describing the weather ("sunny", "snowy", whatever the API makes available like that), and whatever else you think would be useful.
# Add: ask the user for the city to get the forecast for
# Ask the user for a city
city = input("Enter a city to get the 7-day weather forecast:")
# Build the API URL using the city and API key
request_url = f"http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q={city}&days=7&aqi=no&alerts=no"
# Make the request and convert it  to JSON
# response = requests.get(request_url).json()
#You ask the user for a city → 🧍‍♂️ "Hey, what place do you want weather info for?"
# You build the URL with that city → 🛠️ "Okay, now I know where to go."
# You send a request to that URL → 📡 "Give me the weather!"
# You turn the response into readable data → 📦 "Here’s a box of info I can unpack."

#psuedo:creat a function that gets the info the user input, if thet user put in a city parse through response and display the key-value pairs
def get_info(city):
    # Ask the user for a city
    # city = input("Enter a city to get the 7-day weather forecast:")
    # Build the API URL using the city and API key
    request_url = f"http://api.weatherapi.com/v1/forecast.json?key={WEATHER_API_KEY}&q={city}&days=7&aqi=no&alerts=no"
    # Make the request and convert it  to key-value pairs
    response = requests.get(request_url)
    print(response)
    if response.status_code == 200:
        city_data = response.json() #converts it to key-value pairs
        print("city_data:",city_data["location"].keys())#lets me access the location im looking for
        # print("Data retrieved")
        return city_data
    else:print(f"failed to retrieve data{response.status_code}") #tells me the error code when failed to retrieve
city_info = get_info(city)#displays the user input
if city_info: #checks for specific info in the city information
    print(f"name:{city_info["location"]["name"]}")#checks for my country inside location
    # print(f"forcast:{city_info["forecast"]["forecastday"]}"
#TODO: on city_info inside forcast within forecastday displaying the date, go inside the nested "day" key and retrieve the "condition" and "text"  values then get the max temp and min temp:
forecastdays = city_info["forecast"]["forecastday"] #gives me stright access to the dictionary that haves the day,date keys
for day in forecastdays:
    # print("day:",day)
    print("date:",day["date"]) #shows me the date
    print(f"condition:{day["day"]["condition"]["text"]}") #tells me the condition of the day
    # print("check for conditions:",day["day"])
    print(f"avg_temp:{day["day"]["avgtemp_f"]}")
