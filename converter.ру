import requests
from datetime import datetime
usd = float(input("Введите USD: "))
data = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
rate = data["rates"]["RUB"]
rub = usd * rate
print("Курс:", rate)
print("Рублей:", rub)
time = datetime.now().strftime("%Y-%m-%d %H:%M")
with open("history.txt", "a") as f:
    f.write(f"[{time}] {usd} USD = {rub} RUB (курс {rate})\n")
ans = input("Показать историю? (y/n): ")
if ans == "y":
    with open("history.txt", "r") as f:
        lines = f.readlines()
        for line in lines[-10:]:
            print(line) 
