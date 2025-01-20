1. **Lists**
   - **Definition**: A list is an ordered, mutable collection of items.
   - **Syntax**:
     my_list = [1, 2, 3, 'apple', True]
   - **Operations**:
     - **Accessing**:
       my_list[0]  # Output: 1
     - **Appending**:
       my_list.append(4)  # Adds 4 to the end of the list
     - **Sorting**:
       sorted_list = sorted(my_list)  # Sorts the list in ascending order
     - **Slicing**:
       my_list[1:4]  # Output: [2, 3, 'apple']
   - **When to Use**: Store ordered collections, perform computations on data, manipulate data during runtime.

2. **Sets**
   - **Definition**: A set is an unordered, mutable collection with no duplicate elements.
   - **Syntax**:
     my_set = {1, 2, 3, 'apple'}
   - **Operations**:
     - **Add elements**:
       my_set.add(4)  # Adds 4 to the set
     - **Set Operations**:
       - **Union**:
         my_set | {4, 5}  # Output: {1, 2, 3, 'apple', 4, 5}
       - **Intersection**:
         my_set & {2, 3, 4}  # Output: {2, 3}
       - **Difference**:
         my_set - {3}  # Output: {1, 2, 'apple'}
     - **Removing elements**:
       my_set.remove(1)  # Removes 1 from the set
   - **When to Use**: Perform quick membership checks, remove duplicates, store unique items like IP addresses or credentials.

3. **Dictionaries**
   - **Definition**: A dictionary is an ordered, mutable collection that stores key-value pairs.
   - Starting from Python 3.7, dictionaries are insertion-ordered, meaning they maintain the order in which items are added. However, this order is not guaranteed in earlier versions (prior to Python 3.7).

From Python 3.7 onwards, dictionaries remember the order of insertion, so iterating over them will give the same order in which items were inserted.
Before Python 3.7, dictionaries were unordered.

   - **Syntax**:
     my_dict = {'name': 'admin', 'password': '1234'}
   - **Operations**:
     - **Accessing**:
       my_dict['name']  # Output: 'admin'
     - **Adding/Updating**:
       my_dict['email'] = 'admin@example.com'
     - **Removing**:
       del my_dict['password']  # Removes the 'password' key-value pair
     - **Keys, Values, and Items**:
       my_dict.keys()   # Output: dict_keys(['name', 'email'])
       my_dict.values() # Output: dict_values(['admin', 'admin@example.com'])
       my_dict.items()  # Output: dict_items([('name', 'admin'), ('email', 'admin@example.com')])
   - **When to Use**: Store data in a key-value form like user info (e.g., usernames/passwords, IP mappings).

4. **Tuples**
   - **Definition**: A tuple is an ordered, immutable collection of items.
   - **Syntax**:
     my_tuple = (1, 2, 3, 'apple', True)
   - **Operations**:
     - **Accessing**:
       my_tuple[0]  # Output: 1
     - **Concatenation (Joining Tuples)**:
       my_tuple + (4, 5)  # Output: (1, 2, 3, 'apple', True, 4, 5)
     - **Repetition (Multiplying Tuples)**:
       my_tuple * 2  # Output: (1, 2, 3, 'apple', True, 1, 2, 3, 'apple', True)
     - **Slicing**:
       my_tuple[1:4]  # Output: (2, 3, 'apple')
   - **When to Use**: Store fixed collections, returning multiple values, or when you need to prevent accidental modification of data.
