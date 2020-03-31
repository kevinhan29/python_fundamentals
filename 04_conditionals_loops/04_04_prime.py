'''
Print out every prime number between 1 and 100.

'''
is_prime = None                 # flags if current number is a prime or not

print("The following numbers are prime:")
for i in range(2,101):          # go through all numbers from 2-100, (1 can't be prime)
    is_prime = True
    # check to see if current number is divisible by any numbers from 2 to itself, if so then it's not prime
    for j in range(2,i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)
