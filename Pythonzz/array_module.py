# Ưhy we need Arrays?
# Efficiently store and manage large collections of data of same type
# Comsume less memory and offer faster performance than lists for numerical operations 
# Ideal for mathematical and scientific computations where data type consistency is crucial
# Support element-wise operations and indexing for quick data manipulation
# Useful for working with low-level data structures and when interfacing with C or binary files.

# Array Function array(typecode, [value1, value2, ....])

"""Typecode:
'b' -> signed char int
'B' -> unsigned char int
'u' -> Py_unicode
'h' -> signed short int
'H' -> unsigned short int
'i' -> signed int int
'I' -> unsigned int int
'L' -> unsigned long int
'q' signed long long int
'f' float
'd' double"""

# Append Method:
import array
arr = array.array('i', [1, 2, 3])
arr.append(4)

arr.insert(2, 5)
arr.pop()
arr.remove(1)
arr.reverse()
# Heap queue or heapq in Python
import heapq
"""Create (heapify): Convert a regular list into a valid min-heap using heapq.heapify().
Push (heappush): Adds an element to the heap while keeping the heap property intact.
Pop (heappop): Removes and returns the smallest element from the heap.
Peek: Access the smallest element without removing it using heap[0].
Push and Pop (heappushpop): Push a new element and pop the smallest in a single step.
Replace (heapreplace): Pop the smallest and push a new element in one step."""
# [a,b,c] -> Queue

#Heap, tree which is arranged in min, max order
# Create(heapify), Push(heappush), Pop(heappop), Peek(heap[index])
# PushandPop(heappushpop), Replace(heapreplace)


li = [25, 20, 15, 30, 40]
# Convert the list into a heap
heapq.heapify(li) # rearrange the list into min-heap 
max_heap = [-n for n in li] # reverse the position
max_heap = heapq.heapify(max_heap)
# Appending and pop elements
heapq.heapify(li)
heapq.heappush(li, 5)
min = heapq.heappop(li)
# heapq.heappushpop('pop(li)', '5'(push))
maxi = heapq.nlargest(3, li)   # first 3 largest elements
mini = heapq.nsmallest(3, li) 
# heapreplace (li, 5(replace the smallest ele)) # merge (merge two heap )
