print ("Enetr the Numbers")
numbers = []
for num in range (10):
    num = int(input(f"Enter The Number {num+1} :"))
    numbers.append(num)
k=0
squares = []
for num in numbers:
    k = num * num
    squares.append(k)

print ("Actual Numbers",numbers)
print ("Squared Numbers", squares)
    
