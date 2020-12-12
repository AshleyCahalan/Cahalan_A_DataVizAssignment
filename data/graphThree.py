import matplotlib.pyplot as plt
import numpy as np


labels = ["Gold", "Silver", "Bronze"]
men_means = [192, 128, 66]
women_means = [123, 75, 37]

x = np.arange(len(labels))
width = 0.35 

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, color="blue", label='Men')
rects2 = ax.bar(x + width/2, women_means, width, color="hotpink", label='Women')

ax.set_ylabel("Number of Medals")
ax.set_xlabel("Medal Colour")
ax.set_title("Winter Olympic Medals Won by Canadian Athletes")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

fig.tight_layout()

plt.show()