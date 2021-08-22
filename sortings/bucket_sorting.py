"""
- Create buckets and distribute elements of array into the buckets
    -- Number of buckets -> round(sqrt(len(<array>)))
    -- Appropriate bucket -> ceil(<value> * <number of buckets> / <max_value>)
- Sort buckets individually
    -- Any sorting algorithm can be applied
- Merge buckets after sorting

    -- When to use:
        -- When input uniformly distributed over range
    -- When to avoid:
        -- When space is a concern

- Time complexity: O(n^2)
- Space complexity: O(n)
"""
import math


def bucket_sort(_list):
    max_value = max(_list)
    number_of_buckets = round(math.sqrt(len(_list)))
    arr = [[] for i in range(number_of_buckets)]

    for j in _list:
        appropriate_bucket = math.ceil((j * number_of_buckets) / max_value)
        arr[appropriate_bucket - 1].append(j)

    for k in range(number_of_buckets):
        arr[k] = sorted(arr[k])

    t = 0
    for i in range(number_of_buckets):
        for j in range(len(arr[i])):
            _list[t] = arr[i][j]
            t += 1


if __name__ == "__main__":
    my_items = [9, 8, 7, 6, 5, 4, 4, 3, 2, 1]
    bucket_sort(my_items)
    print(my_items)
