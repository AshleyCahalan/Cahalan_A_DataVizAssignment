import matplotlib.pyplot as plt
import numpy as np

# women
x = np.array(["AUT", "CAN", "FIN", "GER", "NOR", "RUS", "URS", "SWE", "SUI", "USA"])
y = np.array([75, 239, 106, 157, 98, 106, 109, 106, 71, 243])
plt.scatter(x, y, color="hotpink")

# men
x = np.array(["AUT", "CAN", "FIN", "GER", "NOR", "RUS", "URS", "SWE", "SUI", "USA"])
y = np.array([59, 328, 328, 203, 359, 157, 331, 327, 214, 410])
plt.scatter(x, y, color="blue")

plt.xlabel("Country")
plt.ylabel("Number of Medals")
plt.title("Winter Olympic Medals Won by Gender")

plt.show()