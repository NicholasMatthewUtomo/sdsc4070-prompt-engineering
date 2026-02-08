### Reasoning Summary
To optimize this function, I first analyzed the nested loop structure to identify the quadratic growth caused by redundant trial divisions. The current implementation performs an exhaustive search for divisors for every integer up to $n$, which is computationally expensive for large datasets. I have determined that replacing this logic with the Sieve of Eratosthenes will significantly reduce the number of operations by marking non-prime numbers in a single pass, leveraging a boolean array for $O(1)$ lookups and $O(n)$ space complexity.

### Identification of the Bottleneck
The line causing the worst time complexity is `for i in range(2, num):`. This inner loop executes for every integer in the outer range, performing trial division up to the value of the current number itself. In a High-Frequency Trading environment, this $O(n^2)$ behavior is unacceptable as it leads to exponential latency increases as the input size grows.

### Mathematical Complexity Analysis
The legacy implementation follows an arithmetic progression for its operation count. For each number $k$ from $2$ to $n$, the inner loop runs up to $k-2$ times. The total number of iterations is defined by the sum $\sum_{k=2}^{n} (k-2)$, which simplifies to $\frac{(n-2)(n-1)}{2}$. This results in a Time Complexity of $O(n^2)$. By implementing the Sieve of Eratosthenes, we optimize the process to $O(n \log \log n)$. This is because we only iterate through multiples of each prime $p$, and the sum of the reciprocals of primes $\sum \frac{1}{p}$ up to $n$ grows at a rate of $\log(\log n)$. This transition from quadratic to near-linear time drastically reduces the CPU cycles required for large $n$.

### Optimized Implementation
```python
def is_prime_sum(n):
    """
    Optimized prime summation using the Sieve of Eratosthenes.
    Time Complexity: O(n log log n)
    Space Complexity: O(n)
    """
    if n < 2:
        return 0
    
    # Initialize a boolean array for the sieve
    # Memory allocation: O(n)
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    # Only need to iterate up to sqrt(n) for the marking phase
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            # Mark multiples of p starting from p*p
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    
    # Summing the indices where sieve[i] is True
    return sum(i for i, is_prime in enumerate(sieve) if is_prime)
```