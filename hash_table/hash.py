"""
- Hashing is a method of sorting and indexing data. The idea behind is to
    allow a large amount of data to be indexed using keys commonly by formulas
    based on the chosen hashing function.
    -   Data is going to stored as a "Key-Value" pair.
    -   We know, searching in an array takes O(N). Even if we use ordered array
        we're able to archive efficiency of O(LogN) since we're be able to
        use Binary Search.

        But looking up in hash tables has an efficiency of O(1) on average.
    
    -   A hash function needs to meet only one criterion to be valid:
        * a hash function must convert the same string to the same number
          number every single time it's applied.

    -   One-directional lookups:
        It needs to be pointed out, that the ability to find any value
        within the hashtable in a single step only works if we know
        the value's key. If we tried to find a particular value without
        having it's key, we'd still have to resort to searching each
        and every key-value pair within the hash table, which is O(N).
        However, the good news is, we have an efficiency of O(1) if we
        know the key.

    -   Collisions
        - Trying to add data to a cell that is already filled is known as
        a collision.
        One classical approach to handling collisions is known as separate
        chaining. When a collision occurs, instead of placing a single value
        in a position(cell), it places in it a reference to an array.
        - There are several techniques to handle it:
            - Direct chaining
                * In this situation, the hash table never fills up.
                * Huge linked list causes performance issues (Looking up Time complexity becomes O(N))
            - Open Addressing:
                * Easy Implementation
                * When Hash Table fills up, creation of new Hash Table affects performance
                    (Time complexity for search operation becomes O(N))
                - Linear Probing
                - Quadratic Probing
                - Double hashing
            
            Notes:
                * If the input size is known we always use "Open Addressing".
                * If we perform deletion operation frequently we use "Direct Hashing".

    -   Efficiency
        Ultimately, a hash table's efficiency depends on three factors:
        - How much data we're storing in the hash table
        - How many cells are available in the hash table
        - Which hash function we're using

        *   If you have a lot of data and only a few cells, there will
            be many collisions and the hash table will lose its efficiency.
        *   A good hash function, therefore, is one that distributes its
            data across all available cells. The more we can spread out our
            data, the fewer collisions we will have.
    
    -   Terminology:
        - Hash Function: A function that can be used to map of arbitrary size
                         to data of fixed size.
        - Key: Input data by a user
        - Hash value: A value that is returned by Hash function.
        - Hash Table: It's a data structure which implements an associative
                      array abstract data type, a structure that can map
                      keys to values.
        - Collision: A collision occurs when two diffrent keys to a hash function
                     produce the same output.
        
        
"""
