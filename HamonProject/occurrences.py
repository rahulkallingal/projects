def occurrences(s):
    # Check if the input is an iterable
    if not hasattr(s, '__iter__') or isinstance(s, str) and isinstance(s, (int, float)):
        raise TypeError("Input must be an iterable")
   
    frequency = {}
    for element in s:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    return frequency


# Test Case 1: Empty string
result = occurrences("")
print("Test Case 1 - Empty string:")
print("Expected:", "Input must be an iterable")
print("Result:", result)

# Test Case 2: Single character
result = occurrences("a")
print("Test Case 2 - Single character:")
print("Expected:", {'a': 1})
print("Result:", result)

# Test Case 3: Repeated characters
result = occurrences("aaa")
print("Test Case 3 - Repeated characters:")
print("Expected:", {'a': 3})
print("Result:", result)

# Test Case 4: Characters with different counts
result = occurrences("aabbccc")
print("Test Case 5 - Characters with different counts:")
print("Expected:", {'a': 2, 'b': 2, 'c': 3})
print("Result:", result)

# Test Case 5: Non-alphabetic characters
result = occurrences("123!@#")
print("Test Case 6 - Non-alphabetic characters:")
print("Expected:", {'1': 1, '2': 1, '3': 1, '!': 1, '@': 1, '#': 1})
print("Result:", result)

# Test Case 6: Mixed characters
result = occurrences("a1b2c3a")
print("Test Case 7 - Mixed characters:")
print("Expected:", {'a': 2, '1': 1, 'b': 1, '2': 1, 'c': 1, '3': 1})
print("Result:", result)

# Test Case 7: Large input
result = occurrences("a" * 1000 + "b" * 500)
print("Test Case 8 - Large input:")
print("Expected:", {'a': 1000, 'b': 500})
print("Result:", result)

# Test Case 8: List of strings
result = occurrences(['apple', 'banana', 'apple', 'orange'])
print("Test Case 1 - List of strings:")
print("Expected:", {'apple': 2, 'banana': 1, 'orange': 1})
print("Result:", result)

# Test Case 9: Tuple of numbers
result = occurrences((1, 2, 2, 3, 3, 3))
print("Test Case 2 - Tuple of numbers:")
print("Expected:", {1: 1, 2: 2, 3: 3})
print("Result:", result)

# Test Case 10: Set with duplicates
result = occurrences(['a', 'b', 'a', 'a', 'b'])
print("Test Case 3 - Set with duplicates:")
print("Expected:", {'a': 3, 'b': 2})
print("Result:", result)