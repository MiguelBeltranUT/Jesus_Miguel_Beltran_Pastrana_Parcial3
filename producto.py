import requests
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    
response = requests.get(url)
        
if response.status_code == 200:
            data = response.json()
            precio_usd = data['bitcoin']['usd']
            
            print(f"Precio de Bitcoin (BTC) en USD: ${precio_usd}")
else:
            print(f"Error al obtener los datos: {response.status_code}")
            
