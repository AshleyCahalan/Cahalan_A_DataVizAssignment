import matplotlib.pyplot as plt

labels = ["CAN", "CZE", "TCH", "FIN", "GER", "FRG", "GBR", "RUS", "EUN", "URS", "SWE", "SUI", "USA"]
other_means = [155, 25, 132, 180, 10, 18, 12, 46, 0, 37, 65, 50, 213]
gold_means = [221, 22, 0, 0, 0, 0, 12, 0, 23, 121, 46, 0, 56]

width = 0.8 

fig, ax = plt.subplots()

ax.bar(labels, other_means, width, label="Bronze & Silver Medals")
ax.bar(labels, gold_means, width, bottom=other_means, label="Gold Medals")

ax.set_ylabel("Number of Medals")
ax.set_xlabel("Country")
ax.set_title("Winter Olympic Medals Won in Ice Hockey")
ax.legend()

plt.show()