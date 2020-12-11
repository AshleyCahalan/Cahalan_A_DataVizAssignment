import matplotlib.pyplot as plt
import numpy as np

# x variable
x = np.array(["USA", "CAN", "NOR", "URS", "SWE", "FIN", "GER", "SUI", "AUT", "RUS"])
# y variable
y = np.array([653, 623, 456, 440, 433, 432, 360, 285, 277, 262,   ])

plt.xlabel("Country")
plt.ylabel("Number of Medals")
plt.title("Number of Medals Won in the Winter Olympics")
plt.bar(x, y, color = "#4CAF50")
plt.show()