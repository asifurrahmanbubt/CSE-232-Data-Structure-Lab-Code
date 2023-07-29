def substring(string, start, end=None):
    if end is None:
        return string[start:]
    return string[start:end]

def string_length(string):
    return len(string)

def find_index(string, sub_string):
    return string.find(sub_string)

def string_compare(str1, str2):
    return str1 == str2

def string_concatenate(str1, str2):
    return str1 + str2

def string_copy(string):
    return string[:]

def string_insert(string, index, sub_string):
    return string[:index] + sub_string + string[index:]

def string_delete(string, start, end):
    return string[:start] + string[end:]

def string_replace(string, old_substring, new_substring):
    return string.replace(old_substring, new_substring)

# Test the functions
sample_string = "Hello, World!"

print("Original String:", sample_string)
print("Substring:", substring(sample_string, 7, 12))
print("Length:", string_length(sample_string))
print("Index of 'World':", find_index(sample_string, "World"))
print("Compare:", string_compare("Hello", "Hello"))
print("Concatenate:", string_concatenate("Hello", " World!"))
print("Copy:", string_copy(sample_string))
print("Insert:", string_insert(sample_string, 5, " Awesome"))
print("Delete:", string_delete(sample_string, 5, 12))
print("Replace:", string_replace(sample_string, "World", "Universe"))
