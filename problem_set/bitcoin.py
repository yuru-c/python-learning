# 無註冊
import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    amount = float(sys.argv[1])

except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin",
        headers={"Authorization": "Bearer YOUR_API_KEY"}
    )
    response.raise_for_status()
except requests.RequestException:
    sys.exit("Request failed")

data = response.json()

prince = float(data["data"]["priceUsd"])

total = amount * prince

print(f"${total:,.4f}")