import math

even_digit_squares =[]

for num in range (1000,9999,2):
    sqrt_num = int(math.sqrt(num))

    if sqrt_num * sqrt_num == num:
        digits =str(num)
        if all(int(d) %2 == 0 for d in digits):
            even_digit_squares.append(num)


print(even_digit_squares)
