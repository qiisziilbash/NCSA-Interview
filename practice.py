import numpy as np
from scipy import fftpack
from matplotlib import pyplot as plt


# # IMPORTANT
# # numpy slices are by reference
# # y = x[1,:].copy()
#
#
#
#
#
# ###
# start = timer()
# # some operation
# end = timer()
# print(end - end)
#
# ###
# a = np.array([[1, 2, 3], [1,2,4]])
# a[0, 1]
# a[0, :]
#
# np.where(a > 2, a, np.nan)
#
# ###
# a = np.array([1,3,4,5,6])
# even_idx = np.argwhere(a%2 == 0).flatten()
# a[even_idx]
#
#
# ###
# np.vstack((a, a))
# np.hstack((a, a))
# np.concatenate((a, a), axis=None) # flattens after
# np.concatenate((a, a), axis=0) # concatanets in spec dim
#
#
# ###
# a = np.array([[1,2,3,4,5], [4,5,6,8,9]])
# a.sum(axis=None) # overall sum  or over axis
# a.mean() #same thing
# a.var()
# a.std()
# a.min()
# a.max()
#
#
#
# ###
# a = np.array([1,2,3], dtype=np.int32)
#
#
# ###
# a = np.array([1, 1, 3])
# b = a
# b[0] = 0 # will change a[0] as well
#
# b = a.copy() # deep copy
#
#
# ###
# a = np.zeros((2,3))
# a = np.full((2,3),4.3)
# eye = np.eye(5)
# a = np.arange(2,8) # 2to7
# a = np.linspace(2,3,5) # 5 elements in [2,3]
#
#
# ###
# a = np.random.random((2,3))
# a = np.random.randn(2, 3) # does not take tuple but dim
# a = np.random.randint(2,4, size= (2,3)) # in range [2,4)
# a = np.random.choice([3,4,5], size=10)
#
#
# ###
