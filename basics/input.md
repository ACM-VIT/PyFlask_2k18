# INPUT

## What is input?

Input is used to read data from user.

## How to take input?

There are two functions in Python that you can use to read data from the user: raw_input() and input()

For python 2.x:<br>
input() is used to read integers.<br>
raw_input() is used to read text(strings) from the user. 

For python 3.x:<br>
input() is used to read strings.<br>
To read strings, it can be typecasted using int(input())

Multiple inputs can be taken in one line using split()

You can store the results from them into a variable.

## Syntax

x = input()<br>
y = raw_input()<br>
a,b,c = input().split()

## Examples

num=input("Enter a number: ")

name=raw_input("Enter your name: ")

You can check out more [examples](./examples) here.

**For more information on Input:**

https://www.pythonforbeginners.com/input/

