import numpy as np
import matplotlib.pyplot as plt1
data = np.genfromtxt('test.txt',delimiter = ',')
name=["Object Temp","Die Temp"]
plt1.xlabel("range")
plt1.ylabel("Temperture");
plt1.title("Temperture plot")
plt1.plot(data)
plt1.legend(name)
plt1.show()
