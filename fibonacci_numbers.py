def fibonacci(n):
    a = 1
    b = 2
    sum = 0
    while a < n:
        a, b = b, a+b
        if a%2==0:
            sum += a
    print(sum)
        
     
fibonacci(4000000)
        