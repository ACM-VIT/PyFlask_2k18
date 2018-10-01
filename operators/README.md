# Python Operators

Operators are used to perform operations on variables and values.

Python divides the operators in the following groups:

- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Identity operators
- Membership operators
- Bitwise operators


## Python Arithmetic Operators

Arithmetic operators are used with numeric values to perform common mathematical operations:

| Operator | Name | Example |
| --- | --- | --- |
| + | Addition | x + y |
| - | Subtraction | x - y |
| \* | Multiplication | x \* y |
| / | Division | x / y |
| % | Modulus | x % y |
| \*\* | Exponentiation | x \*\* y |
| // | Division | x // y |


## Python Assignment Operators

Assignment operators are used to assign values to variables:

| Operator | Example | Same As |
| --- | --- | --- |
| = | x = 5 | x = 5 |
| += | x += 3 | x = x + 3 |
| -= | x -= 3 | x = x - 3 |
| \*= | x \*= 3 | x = x \* 3 |
| /= | x /= 3 | x = x / 3 |
| %= | x %= 3 | x = x % 3 |
| //= | x //= 3 | x = x // 3 |
| \*\*= | x \*\*= 3 | x = x \*\* 3 |
| &amp;= | x &amp;= 3 | x &amp;= 3 |
| \|= | x \|= 3 | x = x \| 3 |
| ^= | x ^= 3 | x = x ^ 3 |
| &gt;&gt;= | x &gt;&gt;= 3 | x = x &gt;&gt; 3 |
| &lt;&lt;= | x &lt;&lt;= 3 | x = x &lt;&lt; 3 |


## Python Comparison Operators

Comparison operators are used to compare two values:

| Operator | Name | Example |
| --- | --- | --- |
| == | Equal | x == y |
| != | Not equal | x != y |
| &gt; | Greater than | x &gt; y |
| &lt; | Less than | x &lt; y |
| &gt;= | Greater than or equal to | x &gt;= y |
| &lt;= | Less than or equal to | x &lt;= y |


## Python Logical Operators

Logical operators are used to combine conditional statements:

| Operator | Description | Example |
| --- | --- | --- |
| and | Returns True if both statements are true | x &lt; 5 and  x &lt; 10 |
| or | Returns True if one of the statements is true | x &lt; 5 or x &lt; 4 |
| not | Reverse the result, returns False if the result is true | not(x &lt; 5 and x &lt; 10) |


## Python Identity Operators

Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

| Operator | Description | Example |
| --- | --- | --- |
| is | Returns true if both variables are the same object | x is y |
| is not | Returns true if both variables are not the same object | x is not y |


## Python Membership Operators

Membership operators are used to test if a sequence is presented in an object:

| Operator | Description | Example |
| --- | --- | --- |
| in | Returns True if a sequence with the specified value is present in the object | x in y |
| not in | Returns True if a sequence with the specified value is not present in the object | x not in y |


## Python Bitwise Operators

Logical operators are used to combine conditional statements:

| Operator | Name | Description |
| --- | --- | --- |
| &amp; | AND | Sets each bit to 1 if both bits are 1 |
| \| | OR | Sets each bit to 1 if one of two bits is 1 |
| ^ | XOR | Sets each bit to 1 if only one of two bits is 1 |
| ~ | NOT | Inverts all the bits |
| &lt;&lt; | Zero fill left shift | Shift left by pushing zeros in from the right and let the leftmost bits fall off |
| &gt;&gt; | Signed right shift | Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off |

You can check out more [examples](./examples) here.

### For more information on Operators:
- https://www.w3schools.com/python/python_operators.asp
- https://realpython.com/python-operators-expressions/
- https://www.youtube.com/watch?v=v5MR5JnKcZI
