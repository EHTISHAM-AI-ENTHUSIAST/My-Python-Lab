# Python Functions

A function is a named block of code that does a specific job. Use functions to organize code and avoid repetition.

Types of functions
- Built-in: Provided by Python (e.g., len(), print(), sum()).
- User-defined: You create these with def.

Syntax
```python
def function_name(parameters):
    """Optional: short description (docstring)."""
    # code
    return value  # optional
```

Notes
- Start with `def`, then the function name and parentheses.
- Parameters (if any) go inside the parentheses.
- Indent the function body.
- Use meaningful names.

Example
```python
def greet(first, last):
    return f"Hello, {first} {last}"

print(greet("Sam", "Wilson"))
```
Output:
```
Hello, Sam Wilson
```

Tips
- Keep functions short and focused (one job).
- Use docstrings to explain what a function does.
- Test functions with different inputs.
