#!/usr/bin/python3
def isWinner(x, nums):
    """Determine the winner after x rounds of the Prime Game."""
    if not nums or x < 1:
        return None  # If there are no rounds or the list is empty, return None

    max_num = max(nums)  # Find the maximum number in the nums list
    primes = [True] * (max_num + 1)  # Create a list to track prime numbers
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers

    # Use the Sieve of Eratosthenes to find all primes up to max_num
    for i in range(2, int(max_num ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False

    # Helper function to count the number of primes up to n
    def count_prime_set_bits(n):
        return sum(primes[:n + 1])

    maria_wins = 0
    ben_wins = 0

    # For each round, determine the winner
    for num in nums:
        if count_prime_set_bits(num) % 2 == 0:
            ben_wins += 1  # Ben wins if the count of primes is even
        else:
            maria_wins += 1  # Maria wins if the count of primes is odd

    # Determine the overall winner based on who won the most rounds
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None  # Return None if it's a tie


if __name__ == "__main__":
    # Test the function with the provided example
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
