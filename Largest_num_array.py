n = int(input("Enter total number of elements: "))
arr = []

for i in range(n):
    arr.append(float(input("Enter Number " + str(i+1) + ": ")))

largest = arr[0]
for i in range(1, n):
    if arr[i] > largest:
        largest = arr[i]

print("\nLargest element =", largest)

'''
Enter total number of elements: 5
Enter Number 1: 12.5
Enter Number 2: 10.0
Enter Number 3: 15.7
Enter Number 4: 8.9
Enter Number 5: 11.2

Largest element = 15.7
'''
