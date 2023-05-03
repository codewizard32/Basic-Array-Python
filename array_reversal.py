num = int(input("Enter the total number of elements: "))
arr = []

for i in range(num):
    arr.append(int(input(f"Enter the element {i+1}: ")))

for i in range(num//2):
    arr[i], arr[num-i-1] = arr[num-i-1], arr[i]

print("Reverse all elements of the array:")
for i in range(num):
    print(arr[i], end=" ")

'''
Enter the total number of elements: 6
Enter the element 1: 1
Enter the element 2: 2
Enter the element 3: 3
Enter the element 4: 4
Enter the element 5: 5
Enter the element 6: 6
Reverse all elements of the array:
6 5 4 3 2 1
'''
