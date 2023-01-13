import sys
import numpy as np
filename = sys.argv[1]
file = open(filename, 'r')
lines = file.readlines()
lst = []
ans = []
for line in lines:
    lst.append(line.split())
for i in range(len(lst)):
    ans.append(int(lst[i][0]))
arr = np.array(ans)
print("Statistics Summary")
print(f"mean {np.mean(arr)}")
print(f"std {np.std(arr)}")
print(f"min {np.min(arr)}")
print(f"max {np.max(arr)}")

