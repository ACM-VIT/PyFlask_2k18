## Dictionary
Dictionaries are Python’s implementation of a data structure that is more generally known as an associative array. A dictionary consists of a collection of key-value pairs. Each key-value pair maps the key to its associated value.

### Defining a dictionary
You can define a dictionary by enclosing a comma-separated list of key-value pairs in curly braces ({}). A colon (:) separates each key from its associated value.

<h5>For eg</h5>

`d = {
    <key>: <value>,
    <key>: <value>,
      .
      .
      .
    <key>: <value>
}`

You can also construct a dictionary with the built-in dict() function. The argument to dict() should be a sequence of key-value pairs. A list of tuple works well for this:
`d = dict([
    (<key>, <value>),
    (<key>, <value),
      .
      .
      .
    (<key>, <value>)
])`
If the key values are simple strings, they can be specified as keyword arguments.
`d = dict(
    <key> = <value>,
    <key> = <value,
      .
      .
      .
    <key> = <value>
)`
## Accessing Dictionary values

After defining a dictionary, we need to access the values assigned. Unlike list, we cannot access elements by their index numbers. So how to access them??

In dictionary, a value is retrieved by specifying its corresponding key in square bracket. `([])`
<h5>For eg:</h5>

`d[<key>]`

Alternatively, we can also use `d.get(<key>)`

#### Updating an entry
To update an entry, just assign a new value to the existing key, i.e.
`d[<key>] = <new_value>`

We can even create new entry in this fashion, i.e.,
`d[<new_key>] = <new_value>`

#### Deleting an entry
Use `del` statement, specifying the key to delete, i.e.
`del d[<key>]`

## Built-in Dictionary Method
As with strings and lists, there are several built-in methods that can be invoked on dictionaries. In fact, in some cases, the list and dictionary methods share the same name. (In the discussion on object-oriented programming, you will see that it is perfectly acceptable for different types to have methods with the same name.)
##### d.clear()
`Clears a dictionary`

##### d.get(<key>[, <default>])
`Returns the value for a key if it exists in the dictionary`

##### d.items()
`Returns a list of key-value pairs in a dictionary`

##### d.keys()
`Returns a list of keys in a dictionary`

##### d.values()
`Returns a list of values in a dictionary`

##### d.pop(<key>[, <default>])
`Removes a key from a dictionary, if it is present, and returns its value`

##### d.update(<obj>)
`Merges a dictionary with another dictionary or with an iterable of key-value pairs`

Please refer `/datatypes/examples/dict.py` for more examples.

For more details and information, please external links and tutorials:
Basics: http://www.tutorialspoint.com/python/python_dictionary.htm

Along with hands on tutorial: https://www.w3schools.com/python/python_dictionaries.asp

