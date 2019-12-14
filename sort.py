import random

test_1 = [10, 8, 3, 12, 1, 5, 7, 3, 15]
test_2 = ["cat", "dog", "apple", "go"]

class Sort:
    ## insertion sort in-place
    def insertion_sort(self, array):
        length = len(array)
        for i in range(length-1):
            for j in range(i+1, 0, -1):
                if (array[j] < array[j-1]):
                    self.swap(array, j, j-1)
        return array

    def swap(self, array, index1, index2):
        temp = array[index1]
        array[index1] = array[index2]
        array[index2] = temp

    def selection_sort(self, array):
        new = []
        while array:
            min_item = min(array)
            new.append(min_item)
            array.remove(min_item)

        return new

    def merge_sort(self, array):
        if len(array) < 2:
            return array

        mid = len(array) // 2
        left, right = self.merge_sort(array[:mid]), self.merge_sort(array[mid:])
        return self.merge(left, right)

    def merge(self, array1, array2):
        new = []
        p1 = 0
        p2 = 0
        while p1 < len(array1) and p2 < len(array2):
            if array1[p1] <= array2[p2]:
                new.append(array1[p1])
                p1 += 1
            else:
                new.append(array2[p2])
                p2 += 1

        if p2 < len(array2):
            new += array2[p2:]

        if p1 < len(array1):
            new += array1[p1:]

        return new

    def quick_sort(self, array, low=0, high=None):
        if high is None:
            high = len(array) -1

        if low < high:
            ploc = self.partition(array, low, high)
            self.quick_sort(array, low, ploc-1)
            self.quick_sort(array, ploc+1, high)

    def partition(self, array, low, high):
        pivot = low
        for i in range(low+1, high):
            if array[i] <= array[low]:
                pivot += 1
                array[i], array[pivot] = array[pivot], array[i]

        array[pivot], array[low] = array[low], array[pivot]
        return pivot


sorter = Sort()
# print(sorter.insertion_sort(test_1))
# print(sorter.insertion_sort(test_2))

# print(sorter.selection_sort(test_1))
# print(sorter.selection_sort(test_2))

# print(sorter.merge_sort(test_1))
# print(sorter.merge_sort(test_2))

# print(test_1, test_2)
# sorter.quick_sort(test_1)
# sorter.quick_sort(test_2)
# print(test_1, test_2)
