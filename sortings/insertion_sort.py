"""
- In case of insertion sort, we divide the given array into two parts
    Taking the first element from unsorted part of the array and find its correct position
    in the sorted part. We do repeat until unsorted part gets empty.

- Time complexity: O(n^2)
- Space complexity: O(1)
"""


def insertion_sort(_list):
    for i in range(1, len(_list)):
        key = _list[i]
        j = i - 1
        while j >= 0 and key < _list[j]:
            _list[j + 1] = _list[j]
            j -= 1
        _list[j + 1] = key


if __name__ == "__main__":
    my_items = [9, 8, 7, 6, 5, -5, 4, 4, 3, 2, 1, 0, -1]
    insertion_sort(my_items)
    print(my_items)
