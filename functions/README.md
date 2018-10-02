# Functions

## Need For Functions

* Code reuse is a very important part of programming in any language. 
* Increasing code size makes it harder to maintain. 
* For a large programming project to be successful, it is essential to abide by the Don't Repeat Yourself, 
or DRY, principle. 

_**FACT** : Bad, repetitive code is said to abide by the WET principle, which stands for Write Everything Twice, or We Enjoy Typing._



## What is a Function?

* A function is a block of code which only runs when it is called.
* You can pass data, known as parameters, into a function.
* A function can return data as a result.
* Any statement that consists of a word followed by information in parentheses is a function call.<br/>
Here are some examples that you've already seen:
```python
print("Hello world!")
range(2, 20)
str(12)
range(10, 20, 3)
```
_**NOTE** : The words in front of the parentheses are function names, and the comma-separated values inside the parentheses are function arguments._


## Functions in Python
* In addition to using pre-defined functions, you can create your own functions by using the def statement.
* Here is an example of a function named my_func.<br/>
It takes no arguments, and prints "spam" three times. It is defined, and then called.<br/>
The statements in the function are executed only when the function is called.<br/>
#### CODE
```python
def my_func():
   print("spam")
   print("spam")
   print("spam")

my_func()
```
#### OUTPUT
```
>>>
spam
spam
spam
>>>
```

_**NOTE** : The code block within every function starts with a colon (:) and is indented._

* You must define functions before they are called, in the same way that you must assign variables before using them.<br/>
#### CODE
```python
hello()

def hello():
    print("Hello world!")
```

#### OUTPUT
```
>>>
NameError: name 'hello' is not defined
>>>
```

## Arguments

* All the function definitions we've looked at so far have been functions of zero arguments, which are called with empty parentheses.<br/>
* However, most functions take arguments.<br/>
* The argument is defined inside the parentheses.<br/>
* The example below defines a function that takes one argument:<br/>
#### CODE
```python
def print_with_exclamation(word):
   print(word + "!")
    
print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")
```

#### OUTPUT
```
>>>
spam!
eggs!
python!
>>>
```

* You can also define functions with more than one argument; separate them with commas.<br/>
#### CODE
```python
def print_sum_twice(x, y):
   print(x + y)
   print(x + y)

print_sum_twice(5, 8)
```
#### OUTPUT
```
>>>
13
13
>>>
```
* Function arguments can be used as variables inside the function definition. 
* However, they cannot be referenced outside of the function's definition. 
* This also applies to other variables created inside a function.<br/>
#### CODE
```python
def function(variable):
   variable += 1
   print(variable)

function(7)
print(variable)
```
#### OUTPUT
```
>>>
8

NameError: name 'variable' is not defined
>>>
```
_**NOTE** : Technically, parameters are the variables in a function definition, and arguments are the values put into parameters when functions are called._

## Functions as Objects
* Although they are created differently from normal variables, functions are just like any other kind of value. 
* They can be assigned and reassigned to variables, and later referenced by those names.<br/>
#### CODE
```python
def multiply(x, y):
   return x * y

a = 4
b = 7
operation = multiply
print(operation(a, b))
```
#### OUTPUT
```
>>>
28
>>>
```

* Functions can also be used as arguments of other functions.<br/>
#### CODE
```python
def add(x, y):
  return x + y

def do_twice(func, x, y):
  return func(func(x, y), func(x, y))

a = 5
b = 10

print(do_twice(add, a, b))
```
#### OUTPUT
```
>>>
30
>>>
```

_**HINT** : As you can see, the function do_twice takes a function as its argument and calls it in its body._

## Links and References
https://www.w3schools.com/python/python_functions.asp <br/>
https://www.tutorialspoint.com/python/python_functions.htm <br/>
https://www.programiz.com/python-programming/function
