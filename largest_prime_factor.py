from re import I


def largest_prime_factor(n):
    i = 3
    primes = []
    while i < n + 1:
        if n%i== 0 and i%2 != 0: 
            rem = n // i
            n = rem
            primes.append(i)
            i += 1
        else:
          i += 1
          print(primes)

    print(max(primes))
            
            
largest_prime_factor(600851475143)            