l = [1,2,3,4,5,6,3,2,1,7]

k = []

for item in l:
    if item not in k:
        k.append(item)
print(k)