numbers = input("Enter the String With Spaces")
list1 = numbers.split()
over=[]

for num in list1:
    if num > 100:
        over.append(num)

print(f"Original String {numbers}")
print(f"Greater than 100 {over}")
        
