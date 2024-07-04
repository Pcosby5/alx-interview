#!/usr/bin/python3
"""0. Prime Game - Maria and Ben are playing a game"""


def isWinner(x, nums):
    """Determines the winner after x rounds of the Prime Game.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers for each round.

    Returns:
        str: Name of the player that
        won the most rounds, or None if there's a tie.
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    # Create a list to determine prime numbers up to the maximum number in nums
    a = [1 for _ in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0  # 0 and 1 are not prime numbers
    for i in range(2, len(a)):
        rm_multiples(a, i)

    # Determine the winner for each round
    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1

    # Determine the overall winner
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """Removes multiples of primes from the list.

    Args:
        ls (list): List indicating prime numbers.
        x (int): Current prime number to remove multiples of.
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break


if __name__ == "__main__":
    # Test the function with the provided example
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
