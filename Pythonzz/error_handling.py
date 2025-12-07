# Python has:
# Syntax Error (missing colons, unmatched parentheses, incorrect indentation)
# Runtime Errors ( TypeError, ValueError, IndexError, KeyError, ZeroDivisionError)
# Logical Errors: result in incorrect logical or output
# Exceptions: Built-in Exceptions (FIleNotFoundError, ImportError)
# Indentation Errors
# eg: FloatingPointError, OverflowError, AssertionError(When you want to assert to user smt, raise assert)
# (assert func, return string)

class InvalidAgeError(Exception):
    def __init__(self, age, msg = "Age must be between 0 and 120:"):
        self.age = age
        self.msg = msg        
        super().__init__(self.msg) # We must call this
    def __str__(self):
        return f"{self.age} -> {self.msg}"

def setage(age):
    if type(age) != 'int':
        raise ValueError("Age must be integer!!!")
    elif age < 0 or age > 120:
        raise InvalidAgeError(age)
    else:
        print(f"Age set to: {age}")
if __name__ == "__main__":
    age = input("Enter your age: ")
    
    
    
    
        