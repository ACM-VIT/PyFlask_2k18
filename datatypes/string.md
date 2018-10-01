# Python strings.

* Python treats  ' ' and " " same unlike c++ 
  
  * Does not support character type : characters are also stored treated as strings of length 1 
    
* Accessing substring and concatenating it with another string
  
  * var = "Pyflask"
      var1 = var [:2] + "thon" 
      This initializez var1 with the value as "python" . (Note [:2] means starting from the first position (0th index) and terminating before 3rd element (2nd index) )
  * x var[1:2] , var[5:10] ?

* escape charaters maybe used 
  
  * non printable characters that can be represented by backslash notation
  * Eg: "\a", "\b" etc.
    
* Built in string methods

  * str.capitalize ():
    > Capitalizes first letter of string
  * str.count(substr,start_index,end_index_optional):
    >Counts how many times str occurs in string or in a substring of string if starting index beg and ending index end are given.
  * str.endswith(substr):
    >Determines if string or a substring of string (if starting index beg and ending index end are given) ends with suffix; returns true if so and false otherwise.
  * str.find(str,start_index,end_index):   
    >Determine if str occurs in string or in a substring of string if starting index beg and ending index end are given returns index if found and -1 otherwise.
  * str.isalnum():
    >Returns true if string has at least 1 character and all characters are alphanumeric and false otherwise.
  * str.isalpha():
    >Returns true if string has at least 1 character and all characters are alphabetic and false otherwise.
  * str.isdigit():
    >Returns true if string contains only digits and false otherwise.
  * str.islower():
    >Returns true if string has at least 1 cased character and all cased characters are in lowercase and false otherwise.
  * str.isnumeric():
    >Returns true if a unicode string contains only numeric characters and false otherwise.
  * str.isupper():
    >Returns true if string has at least one cased character and all cased characters are in uppercase and false otherwise.
  * len(str):
    >Returns the length of the string
  * str.lower():
    >Converts all uppercase letters in string to lowercase.
  * str.strip():
    >Performs both left strip and right strip on string.
  * str.replace(old_str, new_str)
    >Replaces all occurrences of old in string with new or at most max occurrences if max given.   
  * str.join(str):
    >Merges (concatenates) the string representations of elements in sequence seq into a string, with separator string.
  * str.split():
    >Splits string according to delimiter str (space if not provided) and returns list of substrings; split into at most num substrings if given.
                                                              
                                                              
# References

https://www.tutorialspoint.com/python3/python_strings.htm
https://docs.python.org/3/tutorial/introduction.html#strings
