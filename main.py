import requests

def tekshirish(api_url, metod, payload=None, headers=None):
    try:
        response = requests.request(metod, api_url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP error occurred: {errh}")
        return None
    except requests.exceptions.ConnectionError as errc:
        print(f"Error connecting: {errc}")
        return None
    except requests.exceptions.Timeout as errt:
        print(f"Timeout error occurred: {errt}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Something went wrong: {err}")
        return None

# API URL
api_url = "https://jsonplaceholder.typicode.com/posts"

# API metod
metod = "GET"

# API payload
payload = None

# API headers
headers = None

# API response
response = tekshirish(api_url, metod, payload, headers)

if response is not None:
    print(response)
```

Kodda quyidagilar mavjud:

1. `tekshirish` funksiyasi API response ni tekshirish uchun mo'ljallangan.
2. Funksiya `requests` kutubxonasidan foydalanadi.
3. Funksiya API URL, metod, payload va headersni qabul qiladi.
4. Funksiya API response ni tekshiradi va undan foydalanuvchi uchun qaytaradi.
5. Funksiya turli xil xatolar uchun mahsulotni qaytarish uchun `try-except` bloklaridan foydalanadi.
6. API URL, metod, payload va headersni o'zgartirib, API response ni tekshirish uchun funksiya ishlatiladi.
