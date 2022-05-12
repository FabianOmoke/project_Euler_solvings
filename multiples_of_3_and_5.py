# n = int(input("Enter number below which multiples you'd like: \n"))

def multiples_func(n):
    sum = 0
    for x in range (0, n):
        if x%3 == 0 or x%5 == 0:
            sum += x
        else:
            sum+=0
    print(sum)
    
multiples_func(1000)