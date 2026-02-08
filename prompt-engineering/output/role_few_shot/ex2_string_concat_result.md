Analysis:
The current implementation suffers from quadratic time complexity, $O(n^2)$, where $n$ is the total number of characters across all strings. Because strings in Python are immutable, every iteration of the loop creates a entirely new string object and copies the existing content into a new memory buffer. In a high-throughput environment, this triggers excessive allocations and puts unnecessary pressure on the garbage collector.

To optimize this, we must use the `str.join()` method. This approach is significantly more efficient because it performs a two-pass operation: first, it calculates the total memory required for the final string, and second, it performs a single allocation and copies the data directly. This reduces the time complexity to $O(n)$ and minimizes the memory footprint by avoiding intermediate string objects.

Refactored Code:
```python
def build_sentence(words):
    return ' '.join(words).strip() + ' ' if words else ''
```