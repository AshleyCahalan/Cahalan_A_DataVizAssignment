import matplotlib.pyplot as plt

hfont = { 'fontname': 'Lato'}

# plot / chart world population for the past 115 years.

years = [1900, 1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015]

pops = [1.6, 2.5, 2.6, 3.0, 3.3, 3.6, 4.2, 4.4, 4.8, 5.3, 5.7, 6.1, 6.5, 6.9, 7.3]

plt.plot(years, pops, color=(0/225, 100/225, 100/225), linewidth=6.0)

# add some labels
plt.ylabel("Population by Billions")
plt.xlabel("Population Growth by Year")
plt.title("Global Population Growth - 100 Years", pad=20, **hfont)
plt.show()