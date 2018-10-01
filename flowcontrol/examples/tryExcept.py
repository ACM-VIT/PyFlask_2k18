def divide(a): 
    try: 
        result = a[0]//a[1]
        print("Yeah ! Your answer is :", result) 
    except ArithmeticError: 
        print("Sorry ! Arithmetic error occurred ")
    except ZeroDivisionError: #Already Handled by a Parent ArithmeticError exception. So it wont caught any error
        print("Sorry ! You are dividing by zero ")
    except TypeError:
        print("Sorry ! Only numbers are allowed ")
    except: # This will catch every error that is not caught by above exceptions
        print("Sorry ! Some Error occurred")
    else: # this will run if no error occurs
        print("Hurray ! No Error")
    finally: # This will run every time
        print("Program Ends...") 

divide([10,2])
# Yeah ! Your answer is : 5
# Hurray ! No Error
# Program Ends...

divide([10,0]) 
# Sorry ! Arithmetic error occurred
# Program Ends...

divide([10,'a'])
# Sorry ! Only numbers are allowed
# Program Ends...

divide([10])
# Sorry ! Some Error occurred
# Sorry ! Tried to use defined variable
# Program Ends...
