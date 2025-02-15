def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return 'Error: Division by zero'
    except TypeError:
        return 'Error: Invalid input type'

# Example usage with an uncommon error
# Attempting to divide a string by an integer will cause a TypeError, rather than a ZeroDivisionError
result = function_with_uncommon_error('hello', 5)
print(result)