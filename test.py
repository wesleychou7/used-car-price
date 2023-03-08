import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# generate some random data
data = np.random.randn(1000)

# create the histogram
n, bins, patches = plt.hist(data, bins=50, density=True, alpha=0.75)

# calculate the mean and standard deviation of the data
mu, std = norm.fit(data)

# create the normal distribution curve
x = np.linspace(min(bins), max(bins), 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2)

# add labels and a title to the plot
plt.xlabel('Value')
plt.ylabel('Density')
plt.title(r'Histogram of Data with Normal Distribution Overlay ($\mu={:.2f}$, $\sigma={:.2f}$)'.format(mu, std))

# display the plot
plt.show()