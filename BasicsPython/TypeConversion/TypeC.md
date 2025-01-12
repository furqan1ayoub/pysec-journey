# Type Conversions
*This means means converting a value from one data type to another, like changing a number into a string or a string into a number.* 

## 2 ways :- 1) Explicit conversions ; 2) Implicit conversions

```
Common Conversion Functions
int(): Converts to an integer (removes decimal part if a float).
float(): Converts to a float.
str(): Converts to a string.
bool(): Converts to a boolean (True or False).
list(): Converts to a list.
tuple(): Converts to a tuple.
set(): Converts to a set.
```

``` python
# Explicit conversions(Type Casting) : Python automatically converts one data type to another without user intervention.
x = "10"
y = int(x)  # Converts string "10" to integer
print(y, type(y))  # Output: 10, <class 'int'>

# Implicit conversions(Type Coercion): The user manually converts one data type to another using built-in functions.
a = 5
b = 3.2
result = a + b  # Integer a is converted to float automatically
print(result, type(result))  # Output: 8.2, <class 'float'>
```

# Note :- when we talk about type conversion (explicit or implicit), it often involves creating a new value with the desired data type rather than altering the original value.
*Immutable types like strings cannot be changed once created.Python manages memory efficiently by keeping original values separate from their converted forms.*

```python
num = 25          # num references an integer object 25
print(num, type(num))  # Output: 25, <class 'int'>

num = str(num)    # num now references a string object "25"
print(num, type(num))  # Output: "25", <class 'str'>


Here:

First, num was an integer (25).
Then, num was reassigned to reference a string ("25").
```