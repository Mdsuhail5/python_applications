
def prime_checker(number):
    is_prime = True
    for i in range(2, n-1):
        if n % i == 0:
            is_prime = False

    if is_prime is True:
        print(f"The number {n} is prime")
    else:
        print(f"The number {n} is not prime")


n = int(input("Check the number: "))
prime_checker(number=n)
