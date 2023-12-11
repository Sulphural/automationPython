import requests

API_KEY = 'fca_live_21xp78R65qGD7RoC2OXNGEPF3mqa45OyUHW7IFRT'
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("Invalid Currency")
        return None
while True:
    base = input("Enter the base currency (q to quit): ").upper()
    amount = input("Enter how much you want to convert: ").upper()

    if base == "Q":
        break
    
    data = convert_currency(base)
    if not data:
        continue

    del data[base]
    for ticker, value in data.items():
        amttoconvert = value * float(amount)
        print(f"{ticker}: {amttoconvert}")