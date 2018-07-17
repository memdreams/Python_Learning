"""
Implementing different sorting algorithms.
Examples are all descending order.

"""


# Bubble-sort
def bubble_sort(l):
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l


# Selection sort
def selection_sort(l):
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            if l[j] < l[i]:
                l[i], l[j] = l[j], l[i]
    return l


# Insertion sort: descending
def insertion_sort(l=[5,3,8,7,1,-2]):
    n = len(l)
    # traversing the list, the first element in l doesn't need to be sort
    for i in range(1, n):
        # compare the next element to the last element in the sorted list l[:i-1]
        if l[i] < l[i-1]:
            index = i
            # find the right insertion position
            for j in range(i - 1, -1, -1):
                if l[i] < l[j]:
                    index -= 1
            # insert the item l[i] to the right position and delete the original position value
            l.insert(index, l.pop(i))
    return l

# shell sort: (an improved insertion sort, if step=1, it's insertion sort)
def shell_sort(l, step=1):
    n = len(l)
    step = n // 2  # initial the step

    while step > 0:
        # traversing the list, the first element in l doesn't need to be sort
        for i in range(1, n):
            # compare the next element to the last element in the sorted list l[:i-1]
            if l[i] < l[i - 1]:
                print(step)
                index = i-1
                while index >= step and l[i] < l[index]:
                    index -= step
                l.insert(index, l.pop(i))
        step = step // 2
    return l


# Merge Sort: Recursive implementation
def merge_sort(l):
    if len(l) < 2:
        return l
    # divide
    mid = len(l) // 2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])
    # the last time merge
    return merge(left, right)

def merge(left, right):
    result = []
    l, r = 0, 0 # record positions in left and right lists when running
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]  # if left[:] not be tested to the end, add all the left items in result.
    result += right[r:]  # add all the left items in right[:] to the result
    return result


# Quicksort: divide-and-conquer (dig a hole and fill the hole)
def quicksort(l):
    indexL, indexR = 0, len(l)-1
    less, greater, eql = [], [], []
    if len(l) < 2:
        return l
    else:
        pivot = l[0]  # pivot is treated as the start element in l.
        for i in l:
            if pivot > i:  # from right to left to find the 1st item < pivot
                less.append(i)
            elif pivot < i:
                greater.append(i)
            else:
                eql.append(i)

    less = quicksort(less)
    greater = quicksort(greater)
    return less+eql+greater

# <Python Cookbook> solution:
def qsort(l):
    if len(l) <= 1:
        return l
    else:
        pivot = l[0]
        return qsort([i for i in l if i < pivot]) + [i for i in l if i == pivot] + qsort([i for i in l if i > pivot])

# In-place Implementation:
def qsort_inplace(l, start, end):
    '''
    quicksort in-place implementation
        :parameter
        l: the prepared list
        start: the start index of the input list
        end: the end index of the input list
    '''
    if end <= start:
        return
    pivot = l[start]
    indexL, indexR = start, end

    while indexL < indexR:
        while l[indexL] <= pivot and indexL < end:
            indexL += 1
        while l[indexR] >= pivot and indexR > start:
            indexR -= 1
        if indexL < indexR:
            l[indexL], l[indexR] = l[indexR], l[indexL]  #swap

    l[start], l[indexR] = l[indexR], l[start]  # swap pivot

    qsort_inplace(l, start, indexR-1)
    qsort_inplace(l, indexR+1, end)
    return





# import time
if __name__=='__main__':
    ll = [5,3,8,7,1, -2, 4, 2, 2]
    # num = time.clock()
    # print("insertion-sort:", insertion_sort(ll))

    # print(shell_sort(ll))
    # print(merge_sort(ll))
    qsort_inplace(ll, 0, len(ll)-1)
    print(ll)
