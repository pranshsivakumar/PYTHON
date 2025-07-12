import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set(style="darkgrid")

API_KEY = 'your_api_key_here'
CITY = 'Chennai'
URL = f"58a7cab7981cf88089f05f0766547c1e"

response = requests.get(URL)
data = response.json()


forecast_list = data['list']
weather_data = {
    'datetime': [entry['dt_txt'] for entry in forecast_list],
    'temperature': [entry['main']['temp'] for entry in forecast_list],
    'humidity': [entry['main']['humidity'] for entry in forecast_list],
    'weather': [entry['weather'][0]['main'] for entry in forecast_list]
}


df = pd.DataFrame(weather_data)
df['datetime'] = pd.to_datetime(df['datetime'])



plt.figure(figsize=(12, 6))
plt.plot(df['datetime'], df['temperature'], marker='o', color='orange')
plt.title(f"5-Day Temperature Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 6))
sns.lineplot(x='datetime', y='humidity', data=df, marker='o', color='blue')
plt.title(f"5-Day Humidity Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 5))
sns.countplot(x='weather', data=df, palette='Set2')
plt.title(f"Weather Condition Counts in {CITY}")
plt.xlabel("Weather Condition")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
