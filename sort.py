import heapq

tests = [
    [10, 8, 3, 12, 1, 5, 7, 3, 8, 15],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [10, 8, 6, 4, 2, 0],
    ["cat", "dog", "apple", "go"]
]

## insertion sort in-place
def insertion_sort(array):
    length = len(array)
    for i in range(length-1):
        for j in range(i+1, 0, -1):
            if (array[j] < array[j-1]):
                swap(array, j, j-1)

def swap(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

def selection_sort(array):
    # invariant: array[0:index] is sorted, array[index:end] is not sorted yet
    index = 0
    while index < len(array):
        least = None
        least_i = None
        # find smallest element in the unsorted part of the array
        for i in range(index, len(array)):
            if (least is None) or array[i] < least:
                least = array[i]
                least_i = i

        swap(array, index, least_i)
        index += 1

def heap_sort(array):
    new = []
    heapq.heapify(array)
    while array:
        min_item = heapq.heappop(array)
        new.append(min_item)

    return new

# merge sort in-place the part of "array" between start and last, inclusive
def merge_sort(array, start=0, last=None):
    if last is None:
        last = len(array) - 1

    length = last - start + 1
    mid = start + length // 2

    if length < 2:
        return

    merge_sort(array, start, mid-1)
    merge_sort(array, mid, last)
    merge(array, start, mid-1, mid, last)

# merge two sorted, adjacent sub-segments of "array" into one sorted segment
# (uses a temporary buffer but writes the final result into "array")
def merge(array, start1, end1, start2, end2):
    assert start2 == end1+1 # make sure segments are touching
    new = []

    p1 = start1
    p2 = start2

    while p1 <= end1 and p2 <= end2:
        if array[p1] <= array[p2]:
            new.append(array[p1])
            p1 += 1
        else:
            new.append(array[p2])
            p2 += 1

    # finish the ends
    while p1 <= end1:
        new.append(array[p1])
        p1 += 1
    while p2 <= end2:
        new.append(array[p2])
        p2 += 1

    assert len(new) == (end2 - start1) + 1
    array[start1:end2+1] = new

# quicksort array in-place between indexes [low, high] inclusive
def quick_sort(array, low=0, high=None):
    if high is None:
        high = len(array) -1
    if low < high:
        p_loc = partition(array, low, high)
        # after this point, array between [low, high] inclusive looks like:
        # stuff less than array[p_loc] ... array[p_loc] ... stuff greater than array[p_loc]
        quick_sort(array, low, p_loc-1)
        quick_sort(array, p_loc+1, high)

# quicksort parition array[low:high] inclusive, returning final index of pivot
def partition(array, low, high):
    pivot = low # arbitrarily pick array[low] to be the pivot element
    p_val = array[pivot] # value of the pivot
    for i in range(low+1, high+1):
        if array[i] <= p_val: # compare against pivot element
            # if smaller, swap the pivot forward by one element
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]

    array[pivot], array[low] = array[low], array[pivot]
    return pivot

for test in tests:
    answer = sorted(test)
    for method in [insertion_sort, selection_sort, merge_sort, quick_sort, heap_sort]:
        if method is heap_sort:
            # returns new array
            result = method(test)
        else:
            # operates in-place
            temp = test[:] # make a copy
            method(temp)
            result = temp

        if result != answer:
            print('ERROR!', method.__name__, test, result)
