import re
email = input("Input your email here!")
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE): # Form type of email, this require
    # edu at the end, (.....)? is can have or not, bt other must go according to structure
    print("VALID")
else:
    print("Invalid")

name = "Ngo Nhat Anh"
print("Hi, my name is'% a" % name )

# % must be a char and after must be in string or number, list?