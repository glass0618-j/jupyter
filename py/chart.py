import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

hour = ['1h', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h']
pm25 = np.array([34, 37, 30, 27, 35, 38, 43, 42, 37, 35])
pm10 = np.array([46, 49, 41, 40, 81, 90, 53, 52, 55, 51])

plt.figure(figsize=(10,10))
plt.subplot(2,1,1)

for i in range(10):
    if pm25[i] < 15:
        plt.bar(hour[i], pm25[i], color="blue")
    elif 15 <= pm25[i] < 35:
        plt.bar(hour[i], pm25[i], color="green")
    elif 35 <= pm25[i] < 75:
        plt.bar(hour[i], pm25[i], color="orange")
    elif pm25[i] >= 75:
        plt.bar(hour[i], pm25[i], color="red")

plt.title("pm2.5")
plt.subplot(2,1,2)

for i in range(10):
    if pm10[i] < 30:
        plt.bar(hour[i], pm10[i], color="blue")
    elif 30<=pm25[i] <80:
        plt.bar(hour[i], pm10[i], color="green")
    elif 80 <= pm25[i] <150:
        plt.bar(hour[i], pm10[i], color="orange")
    elif pm25[i] >= 150:
        plt.bar(hour[i], pm10[i], color="red")

plt.title("pm10")
plt.show()
