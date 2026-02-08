Analysis: Your current implementation utilizes trial division with a nested loop structure, resulting in a time complexity of O(n²). In a high-frequency environment, this quadratic growth is unacceptable as n scales. Additionally, the repeated use of `list.append()` causes multiple memory reallocations and heap fragmentation. To optimize this, we should implement the Sieve of Eratosthenes, which reduces time complexity to O(n log log n). By using a `bytearray` for the sieve, we minimize memory overhead and improve cache locality compared to a standard list of booleans.

Refactored Code:
```python
def is_prime_sum(n):
    if n < 2:
        return 0
    sieve = bytearray([1]) * (n + 1)
    sieve[0] = sieve[1] = 0
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            sieve[p*p : n+1 : p] = bytearray((n - p*p) // p + 1)
    return sum(i for i, is_p in enumerate(sieve) if is_p)
```