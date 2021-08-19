"""
- Bubble sort is also referred as Sinking sort
- We repeatedly compare each pair of adjacent items and swap them if
    they are in the wrong order.
- Time complexity: O(n^2)
- Space complexity: O(1)
"""


def bubble_sort(_list):
    for i in range(len(_list) - 1):
        for j in range(len(_list) - i - 1):
            if _list[j] > _list[j + 1]:
                _list[j], _list[j + 1] = _list[j + 1], _list[j]


if __name__ == "__main__":
    my_items = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    bubble_sort(my_items)
    print(my_items)
