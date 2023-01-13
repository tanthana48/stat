import sys
import statistics

filename1 = sys.argv[1]
filename2 = sys.argv[2]
text = open(filename1).read()
text1 = open(filename2).read()
data = []
data2 = []
with open(filename1) as f:
    for line in f:
        fields = line.split()
        rowdata = map(float, fields)
        data.extend(rowdata)
mean = sum(data) / len(data)
std = statistics.stdev(data)
biggest = min(data)
smallest = max(data)
with open(filename2) as f2:
    for line in f2:
        fields = line.split()
        rowdata = map(float, fields)
        data2.extend(rowdata)
mean2 = sum(data2) / len(data2)
std2 = statistics.stdev(data2)
biggest2 = min(data2)
smallest2 = max(data2)
finaldata = data + data2
mean3 = sum(finaldata) / len(finaldata)
std3 = statistics.stdev(finaldata)
biggest3 = min(finaldata)
smallest3 = max(finaldata)
print(f"Statistics Summary")
print(f"{filename1}")
print(f"mean1: {mean} std: {std} min: {smallest} max: {biggest} n: {len(data)}")
print(f"{filename2}")
print(f"mean2: {mean2} std: {std2} min: {smallest2} max: {biggest2} n: {len(data2)}")
print(f"Combined:")
print(f"mean3: {mean3} std: {std3} min: {smallest3} max: {biggest3} n: {len(finaldata)}")