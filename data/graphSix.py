import matplotlib.pyplot as plt
import numpy as np

value = np.array([177, 159, 122, 102, 87, 82, 78, 69, 54, 43])
labels = ["USA", "CAN", "NED", "URS", "KOR", "NOR", "RUS", "CHN", "GER", "GDR"]

plt.title("Winter Olympic Medals Won in Skating")
plt.pie(value, labels=labels, shadow=True)
plt.show() 