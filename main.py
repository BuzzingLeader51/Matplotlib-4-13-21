import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

#prepare data
data = np.array([1,2,3,4])
categories = ['a','b','c','d']

#plot figure
fig=plt.figure()

# #plot line graph. third argument optional dots
plt.plot(categories, data, '-o')
# #or
# #bar graph
#plt.bar(categories,data)
#or
#scatter plot
#plt.scatter(data, categories)

# save file
fig.savefig('plot_figure.png')
