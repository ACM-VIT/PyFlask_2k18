# Control Statements

Loop control statements change execution from its normal sequence. When execution leaves a scope, all automatic objects that were created in that scope are destroyed. Python supports the following control statements.

## Continue Statement

It returns the control to the beginning of the loop.

```python
# Prints all letters except 'e' and 'd' 
for letter in 'helloworld':  
    if letter == 'e' or letter == 'd': 
         continue
    print 'Current Letter :', letter 
    var = 10
```

## Break Statement

It brings control out of the loop

```python
for letter in 'helloworld':  
  
    # break the loop as soon it sees 'e'  
    # or 'd' 
    if letter == 'e' or letter == 'd': 
         break
  
print 'Current Letter :', letter 
```

## Pass Statement

We use pass statement to write empty loops. Pass is also used for empty control statement, function and classes.

```python
# An empty loop 
for letter in 'geeksforgeeks': 
    pass
print 'Last Letter :', letter 
```

For more information on loop control statements:

https://www.geeksforgeeks.org/loops-and-loop-control-statements-continue-break-and-pass-in-python/
