import numpy
import matplotlib.pyplot

a=numpy.zeros([3,2])
a[1,1]=1
a[0,1]=4
a[0,0]=7
# print(a)
matplotlib.pyplot.imshow(a, interpolation="nearest")
matplotlib.pyplot.show()