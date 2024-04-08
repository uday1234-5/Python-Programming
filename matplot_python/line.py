import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,3,4,5,6])
y= np.array([5,10,15,20,25,30])
plt.plot(x,y)
plt.show()


import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,3,4,5,6])
y= np.array([5,10,15,20,25,30])
plt.plot(x,y,"o")
plt.show()



import matplotlib.pyplot as plt
import numpy as np
x = np.array([1,2,3,4,5,6])
y= np.array([5,10,15,20,25,30])
plt.plot(x,y,"*")
plt.show()


import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = '>')
plt.show()