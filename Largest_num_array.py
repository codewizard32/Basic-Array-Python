n = int(input("Enter total number of elements: "))
arr = []

for i in range(n):
    arr.append(float(input("Enter Number " + str(i+1) + ": ")))

largest = arr[0]
for i in range(1, n):
    if arr[i] > largest:
        largest = arr[i]

print("\nLargest element =", largest)
