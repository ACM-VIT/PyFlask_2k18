<h1>While loop</h1>
A while loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition. The while loop can be thought of as a repeating if statement.
<br>
<h3>while (boolean_condition)<br> 
{<br>
    // some statements here<br> 
}</h3>
Here, statement(s) may be a single statement or a block of statements. The boolean condition may be any expression, and true is any nonzero value. The loop iterates while the condition is true.
<br>
When the condition becomes false, the program control passes to the line immediately following the loop.
<h3>Ex.</h3> i = 1<br>
while(i < 6)<br>
{<br>
  print(i)<br>
  i = i+1<br>
  }
  <br>
<h3>Output:</h3>
1 2 3 4 5
<br><br>
<h3>Flow Diagram:</h3>
<img src="https://cdn.journaldev.com/wp-content/uploads/2017/10/while-loop-java.png" height="300" width="300">
<br>
<h3>While loop in C</h3>
#include <stdio.h><br>
int main()<br>
{<br>
   int count=1;<br>
   while (count <= 4)<br>
   {<br>
	printf("%d ", count);<br>
	count++;<br>
   }<br>
   return 0;<br>
}<br><br>
<h3>Output:</h3>
1 2 3 4<br><br>
<h3>While loop in Python</h3>
count=1<br>
while(count<=4):<br>
print(count)<br>
count=count+1<br><br>
<h3>Output:</h3>
1 2 3 4<br><br>
<h3>Explanation:</h3><br>
Step 1: The variable count is initialized with value 1 and then it has been tested for the condition.<br>
Step 2: If the condition returns true then the statements inside the body of while loop are executed else control comes out of the loop.<br>
Step 3: The value of count is incremented using ++ operator then it has been tested again for the loop condition.<br><br>
<h3>Now, consider this loop:</h3>
 i = 1<br>
while(i < 6)<br>
{<br>
  print(i)<br>
  }
  <br>
  This is what is known as an <strong>infinite loop</strong>, or never ending loop, meaning this loop never finishes running. This is because the value of i is not changing, it is always =1, so the condition that i<6 will always be true. Hence here 1 will be printed indefinitely.
  <br>
  <br>
 <h1>While with else</h1><br>
  Same as that of for loop, we can have an optional else block with while loop as well.<br>
  The else part is executed if the condition in the while loop evaluates to False.<br>
  The while loop can be terminated with a break statement. In such a case, the else part is ignored. Hence, a while loop's else part runs if no break occurs and the condition is false.<br>
  <h3>Ex.</h3>
  counter = 0<br>
<br>
while counter < 3:<br>
    print("Inside loop")<br>
    counter = counter + 1<br>
else:<br>
    print("Inside else")<br><br>
    <h3>Output:</h3>
    Inside loop<br>
    Inside loop<br>
    Inside loop<br>
    Inside else<br>
