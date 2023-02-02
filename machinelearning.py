from sklearn.linear_model import LinearRegression
import numpy as np
import requests
import numpy as np
import matplotlib.pyplot as plt
n=int(input())

def get_btc_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = requests.get(url)
    data = response.json()
    return float(data['price'])


data = []
time = []
tim = []
for i in range(n):  
    price = get_btc_price()  
    data.append(price)
    time.append([i])
    tim.append(i)
    print(price)
print("Gercek Deger:",get_btc_price())

y = np.array(data)
x = np.array(time)
plt.hist(data)
model = LinearRegression()


model.fit(x, y)

x_test = np.array([[n+1]])  
y_pred = model.predict(x_test)

print("Tahmini Deger: ",y_pred)  
plt.show()

