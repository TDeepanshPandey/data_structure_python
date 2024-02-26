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

#### Additonal Notes - 
- ``print(f'{100 * prob:.2f}%')`` - Better method to print than rounding and adding to string.

