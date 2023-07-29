def simple_pattern_matching(string, pattern):
    matches = []
    for i in range(len(string) - len(pattern) + 1):
        if string[i:i+len(pattern)] == pattern:
            matches.append(i)
    return matches

# Get user input
user_string = input("Enter a string: ")
user_pattern = input("Enter a pattern to find: ")

# Find and print the matches
result = simple_pattern_matching(user_string, user_pattern)

if result:
    print("Pattern found at index(es):", result)
else:
    print("Pattern not found in the string.")
