def main():
    a = [0] * 10
    n = int(input("Enter the number of elements in the array: "))
    print("Enter Elements:")
    for i in range(n):
        a[i] = int(input())

    item = int(input("Enter item to search: "))

    for i in range(10):
        if item == a[i]:
            print(f"Item found at location {i + 1}")
            break
    else:
        print("Item does not exist")


if __name__ == "__main__":
    main()
