# Data Structure Python Udemy Course
 Udemy Course with 150 Excercises in Python

## List 

List is built-in data structure that can store multiple items in a single variable. They are **Ordered, Mutable, Allow Duplicate Members, Heterogeneous**. 

#### Methods:
- *append()*: Adds an element to the end of the list.
- *insert()*: Adds an element at a specific index.
- *remove()*: Removes the first occurrence of a value.
- *pop()*: Removes the element at a specific index.
- *sort()*: Sorts the list.
- *reverse()*: Reverses the list.

## Tuple 

Tuples are used to store multiple items in a single variable. They are **Ordered, Immutable and Allow Duplicate Elements**.

#### Methods:
- *count()*: Returns the number of occurrences of a value.
- *index()*: Returns the index of the first occurrence of a value.

## Set

A set is a built-in data structure that represents an unordered collection of unique elements. They are **Unordered, Mutable, No Duplicate Members, Heterogeneous**

#### Methods:
- *add()*: To add a value.
- *remove()*: To remove a value.
- *discard()*: To discard a value.
- *union()*: Returns a set containing all elements from both sets. **|**
- *intersection()*: Returns a set containing common elements from both sets. **&**
- *difference()*: Returns a set containing elements in the first set that are not in the second set. **-**
- *symmetric_difference()*: Returns a set containing elements that are unique to each set. **^**

Note - There are some other methods like issubset, issuperset. Use autofill to see them.

## Dictionary

A dictionary is a built-in data structure that allows you to store key-value pairs. Dictionaries are **Mutable, Unordered, Key Value Pairs, Unique Keys**.

#### Methods:
- *dict()*: create a dictionary or {}.
- *get()*: get a key in dictionary.
- *pop()* or *del*: to delete a specific key.
- *keys()*: Returns a view object displaying a list of all the keys.
- *values()*: Returns a view object displaying a list of all the values.
- *items()*: Returns a view object displaying a list of key-value tuple pairs.
- *update()*: Updates the dictionary with elements from another dictionary or from key-value pairs.

Note: One can use **|** operator for adding two dictionaries

## Frozenset 

A frozenset is a built-in data structure that is very similar to a regular set, but unlike sets, frozensets are **Immutable, Unordered, No Duplicate Members, Hashable**.

#### Methods:
- *frozenset()* - create frozenset.

## Collections

Collections module in Python is part of the standard library and provides alternative container datatypes to built-in types like list, tuple, set, and dict. These containers are more specialized and come in handy for various specific tasks.

### namedtuple
Namedtuple is a function that returns a new subclass of a tuple. It allows you to give names to the positions in a tuple, providing a way to create simple, self-documenting, and readable code.

### deque
Deque stands for "double-ended queue" and provides fast appends and pops from both ends. It is more flexible than a list for certain use-cases involving frequent insertions and deletions. **Fast Operations, Index Access, Thread-Safe and Bounded Length**. 

#### Methods:
- *append()*: Add an element to the right end.
- *appendleft()*: Add an element to the left end.
- *pop()*: Remove and return an element from the right end.
- *popleft()*: Remove and return an element from the left end.
- *extend()*: Extend deque by appending elements from an iterable at the right end.
- *extendleft()*: Extend deque by appending elements from an iterable at the left end. Note that the iterable's elements will appear in the deque in reverse order.
- *rotate()*: Rotate the deque n steps to the right. If n is negative, rotate to the left.
- *count(x)*: Count the number of deque elements equal to x.
- *reverse()*: Reverse the elements of the deque in-place.
- *clear()*: Remove all elements from the deque.

### Counter
Counter is a dict subclass for counting hashable objects. It's useful for tallying the frequency of elements in collections. **Elements as Keys, Count as Values and Hashable Elements**.

#### Methods:
- *elements()*: Returns an iterator that produces all the elements in the original iterable, repeated according to their count.
- *most_common([n])*: Returns a list of the n most common elements and their counts as tuples. If n is omitted, it returns all elements.
- *subtract([iterable-or-mapping])*: Subtracts the count of elements in the iterable from the existing count.

### defaultdict
defaultdict is another dict subclass that returns a default value for missing keys, simplifying handling of missing keys. **Default Value, Avoids KeyError and Custom Default Values**.

### ChainMap
ChainMap groups multiple dictionaries into a single mapping. Lookups search through the dictionaries from first to last added. **Look-Up Order, Reusability, Dynamic View, Mutable**.

#### Methods:
- *maps*: List of all the constituent mappings
- *new_child()*: Creates a new ChainMap with a new map followed by all previous maps.
- *parents*: Property returning a new ChainMap containing all the maps except the first one.

### UserDict, UserList, and UserString
These are wrapper classes that allow you to more easily extend built-in containers like dict, list, and str.

## Queue 
A queue is a linear data structure in which elements are stored and retrieved in a specific order known as "First-In, First-Out" (FIFO). In a queue, the first element added to the queue is the first one to be removed.

### Stack
A stack is a linear data structure that follows the Last-In, First-Out (LIFO) principle. This means that the last element added to the stack is the first one to be removed.

## Additonal Notes - 
- ``print(f'{100 * prob:.2f}%')`` - Better method to print than rounding and adding to string.
