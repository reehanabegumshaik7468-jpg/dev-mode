arr = [10, 25, 7, 45, 18]

largest = arr[0]

for i in arr:
    if i > largest:
        largest = i

print("Largest element:", largest)