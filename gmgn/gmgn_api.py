import requests

def GetGmgnPrice():
    # Сделайте запрос к API биржи GMGN для получения курса JUP
    url = "https://api.gmgn.com/v1/ticker/JUP-USDT"  # Пример URL для получения данных
    response = requests.get(url)
    
    if response.status_code == 200:
        try:
            data = response.json()
            course = data["price"]  # Предположительно цена находится в ключе "price"
            print(f"Курс JUP: {course}")
            return course
        except KeyError:
            print("Не удалось найти ключ 'price' в ответе.")
        except ValueError:
            print("Ошибка при разборе JSON данных.")
    else:
        print(f"Ошибка запроса: статус-код {response.status_code}")

if __name__ == "__main__":
    GetGmgnPrice()