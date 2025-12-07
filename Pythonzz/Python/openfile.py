import json
def count_words(filename):
    filename = 'alice.txt'

    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print("You don't have this file")
    except FileExistsError:
        print("File is not existing")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {str(num_words)} words ")
import csv
with open('my.csv', 'r+', newline=' ') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(str(row))
import turtle 
def main():
    filename = input("Please enter drawing filename: ")
    t = turtle.Turtle()
    screen = t.getscreen()
    
    file = open(filename, 'r')

def fun(*args):
    return sum(*args)  # *args = ** kwargs (dictionary)
def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, val)
fun (a = 1, b = 2, c = 3)
check = lambda x: 'Positive' if x > 0 else 'Negative' if x < 0 else 'Zero'
li = [lambda arg=x: arg * 10 for x in range (1, 5)]
n = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, n)
multiple = map(lambda x: x * 2, n)
from functools import reduce
multipleall = reduce(lambda x, y: x * y, n) # return final result of 1 * 2 * 3 * 4 * 5 * 6
# 1*2 3 4 5 6 -> 1*2*3 4 5 6 -> 1*2*3*4 5 6 -> 1*2*3*4*5 6 -> 1*2*3*4*5*6    
        
import numpy as np
array = np.array([ [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
print(array.shape) # return 2 dimension of array
print(array.ndim)
print(array.size)
print(array.dtype)