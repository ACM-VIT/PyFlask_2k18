import sys
# Some Examples of the print function in python

# Only _values_ as arguments
a = 3.564
print("a = ", a)
print("a = \n", a)
print("a = ", a)
print("a = \n", a)

### _sep_ argument is used
print("a","b")
print("a","b",sep="")
print(192,168,178,42,sep=".")
print("a","b",sep=":-)")


### _end_ argument is used
for i in range(4):
 print(i)
for i in range(4):
 print(i, end=" ")
for i in range(4):
    print(i, end=" :-) ")

# _file_ argument is used
fh = open("data.txt","w")
print("42 is the answer, but what is the question?", file=fh)
fh.close()
# output into sys.stderr:

print("Error: 42", file=sys.stderr)

# _flush_ argument details
#The file argument must be an object with a write(string) method; if it is not present or None, sys.stdout will be used. Whether output is buffered is usually determined by file, but if the flush keyword argument is true, the stream is forcibly flushed.

#escape sequence examples

print("Hello\nWorld") # New line

print("Hello\tWorld") # Horizontal Tab

print("Hello \'World\' ") # Single quote

print("Hello \"World\" ") #Double quote

print("Hello \\World") # BackSlash