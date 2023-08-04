# 1-D array
arr_1d = [1, 2, 3, 4, 5]

print("1-D Array:")
for value in arr_1d:
    print(f"Element {value} has memory address: {id(value)}")

# 2-D array
arr_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("\n2-D Array:")
for i in range(len(arr_2d)):
    for j in range(len(arr_2d[i])):
        value = arr_2d[i][j]
        print(f"Element {value} at index ({i}, {j}) has memory address: {id(value)}")
