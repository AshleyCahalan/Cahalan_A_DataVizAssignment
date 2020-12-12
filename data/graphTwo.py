import matplotlib.pyplot as plt
import numpy as np

value = np.array([167, 315, 158, 252, 127, 66, 137, 76, 76, 94])
labels = ["USA", "CAN", "NOR", "URS", "SWE", "FIN", "GER", "SUI", "AUT", "RUS"]

plt.title("Winter Olympic Gold Medals Won")
plt.pie(value, labels=labels, shadow=True)
plt.show() 