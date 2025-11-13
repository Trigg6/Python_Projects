numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
list1=[]

for i in numbers:
    if i >100:
        list1.append("Over")
    else:
        list1.append(i)

print(list1)
        
