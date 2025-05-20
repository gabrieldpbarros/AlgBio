import numpy as np
from typing import List

array: List[int] = np.array([[10, 20, 30], [40, 50, 60]])

print(array[1,2])
print(array[0])
for i in array[1]:
    print(i, end=' ')
print('\n')
