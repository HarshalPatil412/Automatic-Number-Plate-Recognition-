#piechart

import matplotlib.pyplot as plt
labels = 'Python', 'C++', 'C', 'Java'
sizes = [245, 210, 130, 215]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0.1, 0.1, 0.1)
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()