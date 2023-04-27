def search(arr, n):
    temp = -1

    for i in range(len(arr)):
        if arr[i] == n:
            print(f"Element found at position: {i + 1}")
            temp = 0
            break

    if temp == -1:
        print("No Element Found")

arr = []
n = int(input("Enter number of elements: "))

for i in range(n):
    element = int(input(f"Enter the element {i + 1}: "))
    arr.append(element)

num = int(input("Please enter an element to search: "))
search(arr, num)
