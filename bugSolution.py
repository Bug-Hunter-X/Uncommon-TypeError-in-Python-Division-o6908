def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except (ZeroDivisionError, TypeError) as e:
        return f'Error: {e}'

# Example usage with improved error handling
result1 = function_with_uncommon_error(10, 0)  # ZeroDivisionError
result2 = function_with_uncommon_error(10, 2)  # Normal division
result3 = function_with_uncommon_error('hello', 5)  # TypeError

print(f"Result 1: {result1}")
print(f"Result 2: {result2}")
print(f"Result 3: {result3}") 