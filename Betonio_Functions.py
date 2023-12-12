def smallest_factor(n):
    # Find the smallest factor of n.
    if n < 2:
        return None  # No factors for numbers less than 2
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i
    return n  # n is a prime number

def find_primes_in_range(start, end):
    # Find prime numbers in the specified range [start, end].
    primes = [num for num in range(start, end + 1) if smallest_factor(num) == num]
    return primes

while True:
    print("Choose an option:")
    print("1. Find the smallest factor of a number.")
    print("2. Find prime numbers in a range.")
    print("0. Terminate the program.")

    choice = int(input("Enter your choice: "))

    if choice == 0:
        print("Program terminated.")
        break

    if choice == 1:
        num = int(input("Enter a number to find its smallest factor: "))
        factor = smallest_factor(num)
        print(f"The smallest factor of {num} is: {factor}")

    elif choice == 2:
        start_range = int(input("Enter the starting number: "))
        end_range = int(input("Enter the ending number: "))

        prime_numbers = find_primes_in_range(start_range, end_range)

        print(f"Prime numbers between {start_range} and {end_range} are: {', '.join(map(str, prime_numbers))}")

    else:
        print("Invalid choice. Please enter a valid option.")
