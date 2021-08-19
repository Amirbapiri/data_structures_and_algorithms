"""
- In case of selection sort we repeatedly find the minimum element
    and move it to the sorted part of array to make unsorted part sorted.
- Time complexity: O(n^2)
- Space complexity: O(1)
- Usage:
    - When to use Bubble sort:
        -- When we have insufficient memory
        -- Easy to implement
    - When to avoid Bubble sort:
        -- When time is a concern
"""


def selection_sort(_list):
    for i in range(len(_list)):
        min_index = i
        for j in range(i + 1, len(_list)):
            if _list[min_index] > _list[j]:
                min_index = j
        _list[i], _list[min_index] = _list[min_index], _list[i]


if __name__ == "__main__":
    my_items = [9, 8, 7, 6, 5, -5, 4, 4, 3, 2, 1, 0, -1]
    selection_sort(my_items)
    print(my_items)
