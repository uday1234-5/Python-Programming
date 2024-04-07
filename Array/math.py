import matplotlib.pyplot as plt
import numpy as np

arr = np.arange(0,10,.1)
data_sin = np.sin(arr)
data_cos = np.cos(arr)
plt.plot(arr,data_sin)
plt.plot(arr,data_cos)
plt.show()

# import numpy as np
# arr = np.arange(1,20,2.4)
# print(arr)