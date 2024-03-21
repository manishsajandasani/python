# append()	    Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the count of a value's occurrences in the list
# extend()	    Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	    Adds an element at the specified position
# pop()	        Removes the element at the specified position
# remove()	    Removes the first item with the specified value
# reverse()	    Reverses the order of the list
# sort()	    Sorts the list


names = ['Manish', 'Sanjay']
print(names)

numbers = [1,2,2,2]
print(numbers)

numbers.append(45)
print(numbers)

numbers.insert(1, 80)
print(numbers)

print(numbers[0])
print(numbers[-1])

names.extend(['Rohit', 'Manav'])
print(names)

names.insert(1, ['Suresh', 'Sunil'])
print(names)

names.pop()
print(names)

names.pop(1)
print(names)

names.remove('Manish')
print(names)

print(numbers.count(2))