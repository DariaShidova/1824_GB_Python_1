import os

main_folder = os.getcwd()
max_size = [100, 1000, 10000, 100000, float("inf")]
result = dict.fromkeys(max_size, 0)

for root, dirs, files in os.walk(main_folder):
    for file in files:
        path = os.path.join(root, file)
        size = os.path.getsize(path)
        group = min(filter(lambda i: size < i, max_size))
        result[group] += 1

print(result)
