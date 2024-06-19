def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True  # 2 and 3 are prime numbers

    if num % 2 == 0 or num % 3 == 0:
        return False  # numbers divisible by 2 or 3 (and greater than 3) are not prime

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")