import numpy as np
lis= list(map(int,input().strip().split()))
arr=np.array(lis)
change_array = arr.reshape(3,3)

print(change_array)     
