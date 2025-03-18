import requests

# response = requests.get("https://api.mexc.com/api/v3/exchangeInfo")
# result = response.json()['symbols']
# print(result)

# for i in result:
#   print(i['symbol'])

import requests
import json


def get_spot_mexc_price(symbol):
    try:
        url = f"https://api.mexc.com/api/v3/ticker/price?symbol={symbol}"
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad requests (4XX, 5XX)

        data = response.json()
        price = data["price"]
        return price

    except requests.exceptions.RequestException as e:
        #print(f"Ошибка при запросе к API MEXC: {e}")
        return None

    except (KeyError, json.JSONDecodeError) as e:
        #print(f"Ошибка при обработке ответа API: {e}")
        return None


def get_futures_mexc_price(symbol):
    try:
        url = f"https://contract.mexc.com/api/v1/contract/fair_price/{symbol}"
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad requests (4XX, 5XX)

        data = response.json()
        price = data['data']['fairPrice']
        return price

    except requests.exceptions.RequestException as e:
        #print(f"Ошибка при запросе к API MEXC: {e}")
        return None

    except (KeyError, json.JSONDecodeError) as e:
        #print(f"Ошибка при обработке ответа API: {e}")
        return None
