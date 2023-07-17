def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def main():
    n = int(input("Enter the number of elements in the array: "))
    a = [0] * n
    print("Enter Elements (in ascending order):")
    for i in range(n):
        a[i] = int(input())

    item = int(input("Enter item to search: "))

    index = binary_search(a, item)
    if index != -1:
        print(f"Item found at location {index + 1}")
    else:
        print("Item does not exist")


if __name__ == "__main__":
    main()
