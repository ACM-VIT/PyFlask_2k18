## Some Examples of the print function in python
You can run these direct commands in the python IDLE to check the usage of these commands

### Only _values_ as arguments
\>>> a = 3.564
\>>> print("a = ", a)
a =  3.564
\>>> print("a = \n", a)
a = 
 3.564
\>>>
\>>> print("a = ", a)
a =  3.564
\>>> print("a = \n", a)
a = 
 3.564


### _sep_ argument is used
\>>> print("a","b")
a b
\>>> print("a","b",sep="")
ab
\>>> print(192,168,178,42,sep=".")
192.168.178.42
\>>> print("a","b",sep=":-)")
a:-)b

### _end_ argument is used
\>>> for i in range(4):
...     print(i)
... 
0
1
2
3
\>>> for i in range(4):
...     print(i, end=" ")
... 
0 1 2 3  
\>>> for i in range(4):
...     print(i, end=" :-) ")
... 
0 :-) 1 :-) 2 :-) 3 :-)

### _file_ argument is used
\>>> fh = open("data.txt","w")
\>>> print("42 is the answer, but what is the question?", file=fh)
\>>> fh.close()
\>>> import sys
\>>> \# output into sys.stderr:
... 
\>>> print("Error: 42", file=sys.stderr)
Error: 42

### _flush_ argument details
The file argument must be an object with a write(string) method; if it is not present or None, sys.stdout will be used. Whether output is buffered is usually determined by file, but if the flush keyword argument is true, the stream is forcibly flushed.