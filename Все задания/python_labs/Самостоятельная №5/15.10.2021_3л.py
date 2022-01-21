array = [1, 3, 12, 3, 1]
max = 0
max_in = 0
for i in range(len(array)):
    if array[i] > max:
        max = array[i]
        max_in = i
min = 0
min_in = 0
for i in range(len(array)):
    if array[i] < min:
        min = array[i]
        min_in = i
array[max_in] = min
array[min_in] = max
print(array)

