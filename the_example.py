import numpy as np
import matplotlib.pyplot as plt

"""
Assume I want to read a metric called SDR (typically used in audio) which I downloaded from tensorboard
"""

# Load the data from a .json file
import json

file = open('sdr.json', 'r')
data = json.load(file)
file.close()

# Filter garbage values from tensorboard and NaNs or Infs
values = [x[2] for x in data if isinstance(x[2], float)]
values = np.array(values)

import my_model_trains as mmt

# I want to compare natural log and power law regression
# I'm gonna use the first 150 values to calculate the regression but gonna extrapolate for 1500
short = values[:150]
regression = mmt.plot_and_regress(np.arange(1, 1 + len(short)), short, 'SDR estimation 150 points', 'epochs', 'SDR',
                                  regressors=['natural_log', 'power_law'], verbose=True, n_values=1200)
plt.show()

# Now gonna compare tot he regression of the whole data
regression = mmt.plot_and_regress(np.arange(1, 1 + len(values)), values, 'SDR estimation 50 points', 'epochs', 'SDR',
                                  regressors=['natural_log', 'power_law'], verbose=True, n_values=1200)

plt.show()
