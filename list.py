# Reverse a list without using built-in reverse functions.
l = [2, 4, 12, 65, 75, 34, 23, 64, 12, 35, 45, 67, 89, 90]
reverse_l = []
for i in range(len(l) -1, -1, -1):
    reverse_l.append(l[i])
print(reverse_l)

# Find the second largest element in a list.
numbers = [12, 45, 7, 89, 34, 89, 56]

largest = second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif largest > num > second_largest:
        second_largest = num

if second_largest == float('-inf'):
    print("There is no second largest element.")
else:
    print("Second largest element:", second_largest)

# Find the second smallest element.
numbers = [12, 45, 7, 89, 34, 89, 56, -99]
numbers.sort()
print(numbers[0])

# OR
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num

print(smallest)

# Rotate the list left by k positions.
list1 = [1, 2, 3, 4, 5]
k = 2
k = k % len(list1)
rotated = list1[k:] + list1[:k] 
print(rotated)

# Merge Two Sorted List
list1 = [2, 5, 1, 2, 4]
list2 = [8, 6, 9, 7]

list1.sort()
list2.sort()

list1.extend(list2)
print(list1)

# Move all zeros to the end.
list3 = [2, 0, 23, 6, 0, 13, 0, 3]
result = []
for num in list3:
    if num != 0:
        result.append(num)
result.extend([0] * list3.count(0))
print(result)

# Find all duplicate elements.
list5 = [1, 2, 3, 4, 5, 2, 3, 4]
duplicates = []
for i in range(len(list5)):
    for j in range(i + 1, len(list5)):
        if list5[i] == list5[j] and list5[i] not in duplicates:
            duplicates.append(list5[i])
print("Duplicate elements:", duplicates)

