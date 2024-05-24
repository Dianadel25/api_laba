import requests
import matplotlib.pyplot as plt

# Виконання запиту до API для отримання інформації про криптовалюти
url = 'https://api.coingecko.com/api/v3/coins/markets'
params = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 10,
    'page': 1,
    'sparkline': False
}
response = requests.get(url, params=params)
data = response.json()

# Витягування необхідних даних
names = [coin['name'] for coin in data]
prices = [coin['current_price'] for coin in data]

# Візуалізація даних
plt.figure(figsize=(10,5))
plt.bar(names, prices, color='green')
plt.xlabel('Cryptocurrency')
plt.ylabel('Price in USD')
plt.title('Top 10 Cryptocurrencies by Market Cap')
plt.xticks(rotation=45)
plt.show()

for coin in data:
    print(f"Name: {coin['name']}, Price: ${coin['current_price']}")

