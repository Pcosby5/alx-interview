0-prime_game.py
# Prime Game

## Description
Maria and Ben are playing a game with a set of consecutive integers starting from 1 up to and including `n`. They take turns choosing a prime number from the set and removing that number and its multiples. The player who cannot make a move loses the game. Maria always goes first and both players play optimally.

## Task
Determine the winner after `x` rounds of the game.

## Requirements
- Allowed editors: vi, vim, emacs
- Files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- Files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the folder is mandatory
- Code should use the PEP 8 style (version 1.7.x)
- Files must be executable

## Implementation

### Initial Checks
- Check if `nums` is empty or `x` is less than 1 and return `None` if true.

### Generate Primes
- Find the maximum number in `nums` to limit the range of the Sieve of Eratosthenes.
- Initialize a list `primes` where each index represents whether the number is prime.
- Use the Sieve of Eratosthenes algorithm to mark non-prime numbers.

### Count Primes Helper Function
- Define a helper function `count_prime_set_bits` to count primes up to `n`.

### Simulate Each Round
- For each number in `nums`, count the primes and determine the winner of that round.
- Increase the win count for Maria or Ben based on whether the count is odd or even.

### Determine Overall Winner
- Compare the total wins of Maria and Ben to determine the overall winner.
- Return `None` if it's a tie.

## Execution
- Make the script executable and run it using the provided main function to see the result.

### Example
```python
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
