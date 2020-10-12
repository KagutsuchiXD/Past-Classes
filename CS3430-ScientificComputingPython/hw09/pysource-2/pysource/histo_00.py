
from matplotlib import pyplot as plt
import numpy as np

## use normal distribution to generate 10,000 points
## centered on 30,000 with an STD = 15,000
incomes = np.random.normal(30000, 15000, 10000)
plt.hist(incomes, 50)
plt.show()
