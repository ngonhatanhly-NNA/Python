import statistics
statistics.mean([100, 90]) # Return average number in the array
import sys
# sys.argv # argument vector
#print('Phiên bản Python hiện tại: ', sys.version)
# print("Python's link: ", sys.executable)
#print("Link to find module: ",)
#for path in sys.path:
#    print('-', path)
#print("Change value: ", sys.argv)
# When you call the python file.py ...... -> It print the argument

class Solution:
    def findSum(self, s1, s2):
        i = len(s1) - 1
        j = len(s2) - 1

        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            d1 = int(s1[i]) if i >= 0 else 0
            d2 = int(s2[j]) if j >= 0 else 0
            current_sum = d1 + d2 + carry
            digit = current_sum % 10
            carry = current_sum // 10
            result.append(str(digit))
            i -= 1
            j -= 1
        final_sum = ''.join(result[::-1])
        return final_sum.lstrip('0') or '0'
# Pathlib module (provide an object-oriented way to work with filesystem paths.
# Unlike traditional os.path which treats path as plain strings, pathlib represents
# them as objects, making operations like path joining, file reading/writing and checking
# existence much cleaner and cross-platform)
# -> Provides an object-oriented alternative to os.path and string-based file handling
# -> Cross-platform compatibility: same code works on Windows, Linux, macOS
# -> Simplifies common tasks like file reading , writing, and directory traversal.
# -> Safer operations: avoids manual string concatenation by offering methods and 
# operator overloading.   
"""--------------------------------------------------------------------------"""
from pathlib import Path
p = Path('/') # creating a path object poiting to root directory
for subdir in p.iterdir():  # sub direction and iterable direction?
    if subdir.is_dir():
        print(subdir) # -. this will return direction
# to find all Python files (.py) within a folder and its subfolders, use
# rglob(Specific global) method from pathlib. It performs a recursive search, making it 
# easy to scan entire directory trees for specific file types.
files = Path.rglob('*.py')
# Navigate inside a Directory Tree
sp = p / 'example.txt' # -> return \example.txt
# QueryPath Properties
"""print("Check if path is absolute: ", sp.is_absolute())
print("Get the file name: ", sp.name)
print("Get the extension: ", sp.suffix)
print("Get the parent directory: ", sp.parent)
"""
# Reading and Writing to a File
with (p / 'example.txt').open('r') as file:
    content = file.read()
    print(content)
with (p/'output.txt').open('w') as file:
    file.write("Hello, GFG!")
# Hierachy of Path Classes in Pathlib:
"""Pure Path|->    -> PurePosixPath    -|-> PosixPath
            |      -> Path             _||
            |->    -> PureWindowPath    -|-> WindownsPath
""" # with no pure, that is concrete
from pathlib import PurePath
# PurePath: It allows you to work with and manipulate path strings. Automatically
# returns a PurePosixPath or PureWindowsPath based on operating system, making it ideal 
# for cross-platform path handling
#.....
# cwd(): current working directory
# exists(): check if path is already existed
# is_dir(): check if path is a direction

"""Os, os.path is necessary for connecting servers"""
import os
os.mkdir("my_directory")  # single directory
os.makedirs("parent_directory/child_directory")  # nested directories
# os.mkdir("my_directory"): makes a folder in the current location.
# os.makedirs(): creates both parent_directory and child_directory if they don’t already exist.
# os.getcwd(): Returns the current directory as a normal string.
# os.getcwdb(): Returns the same path as a byte string.

# Simple rename
os.rename("my_directory", "renamed_directory")

# Rename and create missing parent directories if needed
os.renames("old_dir", "new_parent/new_child/renamed_directory")
# os.rename(src, dst): Renames or moves a file/directory.
# os.renames(src, dst): Same as above, but also creates any missing parents directories in the path.
os.chdir('/home/nikhil/Desktop/') # Changing directory
# os.listdir(path): Lists all files and subdirectories in the given path (non-recursive).
# For recursive listing, use os.walk().