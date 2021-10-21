src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

p = (src[el+1] for el in range(len(src)-1) if src[el+1] > src[el])

print(list(p))
print(type(p))
