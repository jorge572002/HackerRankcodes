def remove_duplicate_letters(s):
    # Map to store the last index of each character
    last_index = {c: i for i, c in enumerate(s)}
    # Set to keep track of seen characters
    seen = set()
    # List to build the result string
    result = []
    
    for i, c in enumerate(s):
        # If the character is already in the result, continue
        if c in seen:
            continue
        
        # Maintain lexicographically maximum result
        while result and result[-1] < c and last_index[result[-1]] > i:
            seen.remove(result.pop())
        
        result.append(c)
        seen.add(c)
    
    return ''.join(result)

# Test case
input_string = "aabcb"
output_string = remove_duplicate_letters(input_string)
print("Result:", output_string)  # Output should be "acb"
