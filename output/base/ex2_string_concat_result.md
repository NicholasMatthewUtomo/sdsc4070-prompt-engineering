REFACTORED CODE

def build_sentence(words):
    return ' '.join(words)

PERFORMANCE IMPROVEMENTS

The original code is inefficient because strings in Python are immutable. Every time the code executes the line that adds a word to the result string, Python cannot simply modify the existing string in place. Instead, it must create a brand-new string object in memory and copy every single character from the old string and the new word into that new location. As the sentence grows longer, the amount of copying increases significantly, leading to a performance bottleneck known as quadratic time complexity.

The refactored version uses the built-in join method, which is specifically optimized for this task. Instead of repeated copying, the join method first calculates the total length of the final string. It then allocates the necessary memory all at once and copies the words into their respective positions in a single pass. This approach avoids the overhead of creating multiple intermediate string objects, making the function run much faster, especially when dealing with large lists of words.

COMPLEXITY ANALYSIS

The time complexity of the refactored code is O(n), where n is the total number of characters across all words in the input list. This is considered linear complexity because the algorithm only needs to look at each character a constant number of times to place it into the final string. This is a major improvement over the original code's O(n squared) complexity.

The space complexity is also O(n). The function requires an amount of memory proportional to the total length of the words to store and return the final concatenated string. Since no unnecessary intermediate strings are created during the process, this is the most memory-efficient way to perform the operation.