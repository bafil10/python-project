primes = []
num = int(input("Enter a number: "))
for possiblePrime in range(2, num): 
    isPrime = True
    for num in range(2, possiblePrime):
        if possiblePrime % num == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(possiblePrime)
        
