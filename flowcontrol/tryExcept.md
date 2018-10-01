
# Try Except
In python there are two kinds of errors
* **Syntax Error** : Also known as Parsing Errors, most basic. Arise when the Python parser is unable to understand a line of code.
* **Exception** : Errors which are detected during execution. eg – ZeroDivisionError.

>Try Except is used to handle exception

The `try` block lets you test a block of code for errors.
The `except` block lets you handle the error.
The `finally` block lets you execute code, regardless of the result of the try- and except blocks.

## Need of Exception Handling
When an error occurs, or exception as we call it, Python will normally stop and generate an error message. Since we can't let our application (supoose a web server) to crash, we use exception handling.

Exception handling let us to have control on what will happen when our program will encounter an err instead of stoping the execution.

## Sequense of Try and Except execution

*   First `try` clause is executed i.e. the code between `try` and `except` clause.
* If there is no exception, then only `try` clause will run, `except` clause is finished.
* If any exception occured, `try` clause will be skipped and `except` clause will run.
* If any exception occurs, but the `except` clause within the code doesn’t handle it, it is passed on to the outer `try` statements. If the exception left unhandled, then the execution stops.
* A `try` statement can have more than one `except` clause

### Other Keywords
* #### Else
    You can use the else keyword to define a block of code to be executed if no errors were raised
    ```python
    try:
        print("Hello")
    except:
        print("Something went wrong")
    else:
        print("Nothing went wrong")
    ```
* #### Finally
    The finally block, if specified, will be executed regardless if the try block raises an error or not.
    ```python
    try:
        print(x)
    except:
        print("Something went wrong")
    finally:
        print("The 'try except' is finished")
    ```
    
## List of Exception Errors
Here is a full Python exception class hierarchy view
* BaseException
  * Exception
    * ArithmeticError
    * FloatingPointError
    * OverflowError
    * ZeroDivisionError
  * AssertionError
  * AttributeError
  * BufferError
  * EOFError
  * ImportError
    * ModuleNotFoundError
  * LookupError
    * IndexError
    * KeyError
  * MemoryError
  * NameError
    * UnboundLocalError
  * OSError
    * BlockingIOError
    * ChildProcessError
    * ConnectionError
      * BrokenPipeError
      * ConnectionAbortedError
      * ConnectionRefusedError
      * ConnectionResetError
    * FileExistsError
    * FileNotFoundError
    * InterruptedError
    * IsADirectoryError
    * NotADirectoryError
    * PermissionError
    * ProcessLookupError
    * TimeoutError
  * ReferenceError
  * RuntimeError
    * NotImplementedError
    * RecursionError
  * StopIteration
  * StopAsyncIteration
  * SyntaxError
    * IndentationError
      * TabError
  * SystemError
  * TypeError
  * ValueError
    * UnicodeError
      * UnicodeDecodeError
      * UnicodeEncodeError
      * UnicodeTranslateError
  * Warning
    * BytesWarning
    * DeprecationWarning
    * FutureWarning
    * ImportWarning
    * PendingDeprecationWarning
    * ResourceWarning
    * RuntimeWarning
    * SyntaxWarning
    * UnicodeWarning
    * UserWarning
  * GeneratorExit
  * KeyboardInterrupt
  * SystemExit

## Major Exception Types Overview

Exception   | Description
------------- | -------------
ArithmeticError  | The base class for the variety of arithmetic errors, such as when attempting to divide by zero, or when an arithmetic result would be too large for Python to accurately represent.
AssertionError | This error is raised when a call to the [`assert`] statement fails.
AttributeError | Python’s syntax includes something called `attribute references`, which is just the Python way of describing what you might know of as `dot notation`. In essence, any `primary token` in Python (like an identifier, literal, and so forth) can be written and followed by a period (.), which is then followed by an `identifier`. That syntax (i.e. primary.identifier) is called an attribute reference, and anytime the executing script encounters an error in such syntax an AttributeError is raised.
BufferError | Python allows applications to access low level memory streams in the form of a `buffer`. For example, the bytes class can be used to directly work with `bytes` of information via a memory buffer. When something goes wrong within such a buffer operation a BufferError is raised.
EOFError | Python’s EOFError is raised when using the `input()` function and reaching the end of a file without any data.
ImportError | Modules are usually loaded in memory for Python scripts to use via the import statement (e.g. import car from vehicles). However, if an `import` attempt fails an `ImportError` will often be raised.
LookupError | Like `ArithmeticError`, the LookupError is generally considered a base class from which other subclasses should inherit. All `LookupError` subclasses deal with improper calls to a collection are made by using invalid `key` or `index` values.
MemoryError | In the event that your Python application is about to run out of memory a `MemoryError` will be raised. Since Python is smart enough to detect this potential issue slightly before all memory is used up, a `MemoryError` can be `rescued` and allow you to recover from the situation by performing garbage collection of some kind.
NameError | Raised when trying to use an `identifier` with an invalid or unknown name.
OSError | This error is raised when a system-level problem occurs, such as failing to find a local file on disk or running out of disk space entirely. `OSError` is a parent class to many subclasses explicitly used for certain issues related to operating system failure, so we’ll explore those in future publications.
ReferenceError | Python includes the weakref module, which allows Python code to create a specific type of reference known as a `weak reference`. A weak reference is a reference that is not “strong” enough to keep the referenced object alive. 
RuntimeError | A RuntimeError is typically used as a `catchall` for when an error occurs that doesn’t really fit into any other specific error classification.
StopIteration | If no `default` value is passed to the next() function when iterating over a collection, and that collection has no more iterated value to retrieve, a `StopIteration` exception is raised. Note that this is not classified as an `Error`, since it doesn’t mean that an error has occurred.
StopAsyncIteration | As of version 3.5, Python now includes coroutines for `asynchronous transactions` using the `async and await` syntax. As part of this feature, collections can be `asynchronously` iterated using the __anext__() method. The __anext__() method requires that a StopAsyncIteration instance be raised in order to halt async iteration.
SyntaxError | Just like most programming languages, a `SyntaxError` in Python indicates that there is some `improper syntax` somewhere in your script file. A SyntaxError can be raised directly from an executing script, or produced via functions like `eval()` and `exec()`.
SystemError | A `generic error` that is raised when something goes wrong with the `Python interpreter` (not to be confused with the `OSError`, which handles operating system issues).
TypeError | This error is raised when attempting to perform an `operation` on an `incorrect object type`.
ValueError | Should be raised when a function or method receives an argument of the correct type, but with an actual value that is `invalid` for some reason.
Warning | Another parent class to many subclasses, the Warning class is used to `alert` the user in non-dire situations.
 