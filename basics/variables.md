# Variables
* Variables play a very important role in most programming languages, and Python is no exception. 
* A variable allows you to store a value by assigning it to a name, which can be used to refer to the value later in the program. 
* To assign a variable, use one equals sign. Unlike most lines of code we've looked at so far, it doesn't produce any output at the Python console.
#### Example

```
>>> x = 7
>>> print(x)
7
>>> print(x + 3)
10
>>> print(x)
7
```
_**NOTE** : You can use variables to perform corresponding operations, just as you did with numbers and strings. As you can see, the variable stores its value throughout the program._

* Variables can be reassigned as many times as you want, in order to change their value. 
In Python, variables don't have specific types, so you can assign a string to a variable, and later assign an integer to the same variable.
#### Example
```
>>> x = 123.456
>>> print(x)
123.456
>>> x = "This is a string"
>>> print(x + "!")
This is a string!
```
_**NOTE** : However, it is not good practice. To avoid mistakes, try to avoid overwriting the same variable with different data types._
## Variable Names
* Certain restrictions apply in regard to the characters that may be used in Python variable names. 
* The only characters that are allowed are letters, numbers, and underscores. Also, they can't start with numbers.
* Not following these rules results in errors.
```
>>> this_is_a_normal_name = 7

>>> 123abc = 7
SyntaxError: invalid syntax

>>> spaces are not allowed
SyntaxError: invalid syntax
```
## Variable Assignment
* Trying to reference a variable you haven't assigned to causes an error. 
* You can use the del statement to remove a variable, which means the reference from the name to the value is deleted, and trying to use the variable causes an error. 
* Deleted variables can be reassigned to later as normal.

#### Example
```
>>> foo = "a string"
>>> foo
'a string'
>>> bar
NameError: name 'bar' is not defined
>>> del foo
>>> foo
NameError: name 'foo' is not defined
```
* You can also take the value of the variable from the user input.
```
>>> foo = input("Enter a number: ")
Enter a number: 7
>>> print(foo)
7
```
