num = int(input("Enter the total number of elements: "))
arr = []

for i in range(num):
    arr.append(int(input(f"Enter the element {i+1}: ")))

for i in range(num//2):
    arr[i], arr[num-i-1] = arr[num-i-1], arr[i]

print("Reverse all elements of the array:")
for i in range(num):
    print(arr[i], end=" ")
