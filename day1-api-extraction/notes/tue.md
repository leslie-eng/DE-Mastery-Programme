## what is an exception
An exception is an error that occurs while a program is executing 
eg number = int("hello") -> Python raises ValueError: invalid literal for int()
to handle errors we use try and except blocks
'''
try:
    # code that might fail
except:
    # What to do if an error occurs

--> try:
        age = int(input("Enter your age: "))
        print(f"You are  {age} years old")
    except:
        print("something went wrong")
'''
Catch specific exceptions
avoid using bare except: unless you have a good reason

'''
try:
    age = int(input("Enter your age"))
except ValueError:
    print("please enter a valid number)
'''
Exception                       When it occurs
ValueError                  Valid type, but invalid value
TypeError                   Operation performed on an incompatible type
KeyError                    Dictionary key doesn't exist
IndexError                  List index is out of range
AttributeError              Object doesn't have the requested attribute

else: Executes when no exception occurs
finally: Executes whether an exception occurs or not

'''
try:
    number = int("25")

except ValueError:
    print("Invalid number")

else:
    print("Conversion successful:", number)

finally:
    print("Execution completed.")
'''

Three rules worth remembering
1. Catch specific exceptions. Don't hide every possible error with a generic except.
2. Don't use exceptions to replace ordinary logic. If you can easily check whether a key exists, do so when appropriate.
3. Don't silently swallow errors. Sometimes you should log the error or re-raise it rather than returning None.