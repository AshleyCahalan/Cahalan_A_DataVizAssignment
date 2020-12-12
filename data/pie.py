import matplotlib.pyplot as plt

hfont = { 'fontname': 'Arial'}

value = [277, 623, 432, 360, 456, 262, 440, 433, 285, 653]
labels = ["AUS", "CAN", "FIN", "GER", "NOR", "RUS", "URS", "SWE", "SUI", "USA"]
# colors = ["green", "gold"]

# explode = (0, 0.1)

# colors=colors, explode=explode

plt.pie(value, labels=labels)
plt.title("Top 10 Medal Earning Countries at the Winter Olympic Games 1924-2014", **hfont)
plt.show() # generate the pie chart