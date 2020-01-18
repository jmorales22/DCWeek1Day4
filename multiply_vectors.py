#Multiplies a two vectors of the same lenth together to get a third vector

v1 = [1, 2, 3, 4, 10]
v2 = [2, 4, 6, 3, 12]
v3 = []

i = 0

if i < len(v1):
    for num in v1:
        num3 = v1[i]*v2[i]
        v3.append(num3)
        i += 1
print(v3)