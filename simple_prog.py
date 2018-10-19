'''
Created on 19-Oct-2018

@author: Nalini.V
'''
from matplotlib import pyplot as plt



x = [1,2,3]
y = [4,5,8]

plt.plot(x,y, color='g', label='bar1')
plt.legend()
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("test")
plt.show()