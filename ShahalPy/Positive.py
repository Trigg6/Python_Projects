print ("Enetr the integers")
numbers = []
for num in range (10):
    num = int(input(f"Enter The Number {num+1} :"))
    numbers.append(num)
    
positive_numbers = []
for num in numbers :
    if num > 0 :
        positive_numbers.append(num)
        
print("Original List:",numbers)
print("Positive  List:",positive_numbers)

        
