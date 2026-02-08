Analysis:
The current implementation relies on a manual loop within the Python interpreter, which introduces significant bytecode overhead for each iteration. While the time complexity is $O(n)$, the constant factors are high because the addition and iteration are not vectorized or handled at the C-layer. Additionally, frequent updates to a global variable can lead to cache invalidation issues in high-concurrency environments, though the primary bottleneck here is the execution speed of the loop itself. By utilizing the built-in `sum()` function, we offload the summation to highly optimized C code, reducing the number of interpreter instructions.

Refactored Code:
```python
total = 0
def add_to_total(nums):
    global total
    total += sum(nums)
    return total
```