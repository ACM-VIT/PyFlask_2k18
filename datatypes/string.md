                                                    Python strings.

1. Python treats  ' ' and " " same unlike c++ 
    - Does not support character type : characters are also stored treated as strings of length 1 
    
2. Accessing substring and concatenating it with another string
    - var = "Pyflask"
      var1 = var [:2] + "thon" 
      This initializez var1 with the value as "python" . (Note [:2] means starting from the first position (0th index) and terminating before 3rd element (2nd index) )
    - x var[1:2] , var[5:10] ?

3. escape charaters maybe used 
    - non printable characters that can be represented by backslash notation
    - example \a,\b\ etc
    
4. Built in string methods 
    - str.capitalize ()
    - str.count(substr,start_index,end_index_optional)
    - str.endswith(substr)
    - str.find(str,start_index,end_index)                    (returns -1 if not found)
    - str.isalnum()
    - str.isalpha()
    - str.isdigit()
    - str.islower()
    - str.isnumeric()
    - str.isupper()
    - len(str)
    - str.lower()
    - str.upper()
    - str.strip()
    - str.replace(old_str, new_str)   
    - str.join(str)                                           (For example. "_".join("hello") gives "h_e_l_l_o"
                                                              )
    - str.split()                                             (returns a list of strings that were separated by spaces in the string
                                                               for example. if i have a string A="we are delighted to see u" , then we                                                                  get A= ["we","are","delighted","to","see","u"]
                                                              )
                                                              
                                                              
     References : https://www.tutorialspoint.com/python3/python_strings.htm
                  https://docs.python.org/3/tutorial/introduction.html#strings

   
                                                              
