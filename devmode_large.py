#creating a list
list=list(map(int,input("Enter the elements : ").split()))
largest=list[0]

for i in list:
    if i>largest:
        largest=i

print("Largest element:", largest)
