# Print prime numbers below 100
def is_prime(num):
    divisor = int(num/2)+1
 
    for i in range(2,divisor):
        if num % i == 0:
            return False
    return True
 
for num in range(2,100):
    if is_prime(num):
        print(num)
