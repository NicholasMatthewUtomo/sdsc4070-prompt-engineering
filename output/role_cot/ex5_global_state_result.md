### Reasoning Summary
I will analyze the execution overhead of the Python bytecode interpreter during manual iteration. By identifying the linear scaling of the loop and the constant-time overhead of global variable access, I will determine that a built-in summation function provides a more efficient implementation by leveraging C-level execution.

### Identification of Performance Bottleneck
The line causing the primary performance bottleneck is the loop structure: `for x in nums:`. While the addition operation itself is necessary, the manual iteration through the list in the Python interpreter introduces significant overhead for each element processed. In a high-frequency environment, the cumulative cost of fetching each object from the list and executing the corresponding bytecode instructions for the addition operation results in suboptimal throughput.

### Mathematical Complexity and Analysis
The time complexity of the legacy function is $O(N)$, where $N$ represents the number of elements in the input collection. Mathematically, the total execution time can be modeled as $T(N) = N \cdot (c_{iter} + c_{add}) + c_{init}$, where $c_{iter}$ is the overhead of the interpreter's loop mechanism and $c_{add}$ is the cost of the addition. In standard Python, $c_{iter}$ is relatively large because the virtual machine must perform type checking and dynamic dispatch for every iteration. By moving the summation to a built-in function implemented in C, we effectively minimize the constant factor $k$ in our $O(k \cdot N)$ complexity, significantly reducing the execution time even though the asymptotic complexity remains linear.

### Optimized Python Code
```python
def add_to_total_optimized(nums: list[int], current_total: int = 0) -> int:
    """
    Optimized summation using Python's C-implemented sum function.
    Avoids global state to ensure thread safety and better memory locality.
    """
    return current_total + sum(nums)
```