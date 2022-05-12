def sum_square_difference(n):
    sum = 0
    sum_of_squares = 0
    for x in range(1, n + 1):
        sum_of_squares += x**2
        sum +=x
    square_of_sums = sum**2
    print(sum_of_squares)
    print(square_of_sums - sum_of_squares )
        
sum_square_difference(100)
        