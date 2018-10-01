## What does print function do:
The print function in Python is a function that outputs to your console window whatever you say you want to print out. At first blush, it might appear that the print function is rather useless for programming, but it is actually one of the most widely used functions in all of python.The reason for this is that it makes for a great debugging tool.
"Debugging" is the term given to the act of finding, removing, and fixing errors and mistakes within code.
If something isn't acting right, you can use the print function to print out what is happening in the program. Many times, you expect a certain variable to be one thing, but you cannot see what the program sees. If you print out the variable, you might see that what you thought was, was not.

## Print function syntax:
print(value1, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
where parameters are seperated by a ,

*Parameter	Description*
* object(s)	Any object, and as many as you like. Will be converted to string before printed
* sep='separator'	(Optional)Specify how to separate the objects, if there is more than one. Default is ''
* end='end'	(Optional)Specify what to print at the end. Default is '\n' (line feed)
* file	(Optional)An object with a write method. Default is sys.stdout
* flush	(Optional)A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False

## Use of escape sequence
In Python strings, the backslash "\" is a special character, also called the "escape" character. It is used in representing certain whitespace characters: "\t" is a tab, "\n" is a newline, and "\r" is a carriage return. ... Finally, "\" can be used to escape itself: "\\" is the literal backslash character.

Take a look at [Examples](./basics/examples/print.py) to make things more clear to you

You can know more about the print function :
1. Print function use : https://pythonprogramming.net/python-tutorial-print-function-strings/
2. Syntax and attributes of print function : https://www.w3schools.com/python/ref_func_print.asp
3. Some examples of print function : https://www.programiz.com/python-programming/methods/built-in/print