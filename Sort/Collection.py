'''
    十大排序手写熟悉下
    @author PingJing
'''

import math

arr = [2, 5, 3, 5, 4]

'''
    数组元素交换
'''


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr

# 选择排序类

'''
    简单选择排序
'''


def selectionSort(arr):
    for i in range(0, len(arr) - 1):
        minindex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minindex]:
                minindex = j
        swap(arr, i, minindex)
    return arr
# print(selectionSort(arr))

# 交换排序类
'''
    冒泡排序
'''


def bubbleSort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                swap(arr, i, j)
    return arr


'''
    快速排序
'''


def quickSort(arr, start, end):
    if start >= end:
        return
    low = start
    high = end
    mid = arr[start]    # 设置第一个数为参考点
    while low < high:
        while low < high and arr[high] >= mid:  # 从右往左遍历
            high -= 1
        arr[low] = arr[high]    # 比参考点小的数交换到参考点左
        while low < high and arr[low] <= mid:   # 从左往右遍历
            low += 1
        arr[high] = arr[low]    # 比参考点大的数交换到参考点右
    arr[low] = mid
    quickSort(arr, start, low - 1)  # 递归参考点左侧子序列
    quickSort(arr, low + 1, end)    # 递归参考点右侧子序列
    return arr
# print(quickSort(arr, 0, len(arr) - 1))

# 插入排序类
'''
    插入排序
'''


def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            swap(arr, j, j - 1)
            # temp = arr[j - 1]
            # arr[j - 1] = arr[j]
            # arr[j] = temp
            j -= 1
    return arr
# print(insertionSort(arr))

'''
    希尔排序
'''


def shellSort(arr):
    gap = math.floor(len(arr) / 2)  # 间隔
    while gap > 0:
        gap = math.floor(gap / 2)
        for i in range(gap, len(arr)):
            j = i
            while j - gap >= 0 and arr[j] < arr[j - gap]:
                # 插入排序采用交换法
                swap(arr, j, j - gap)
                j -= 1
    return arr
# print(shellSort(arr))

# 归并排序
'''
    归并排序
'''


def mergeSort(arr):
    if len(arr) < 2:
        return arr
    mid = math.floor(len(arr) / 2)
    left, right = arr[0:mid], arr[mid:]
    return merge(mergeSort(left), mergeSort(right))     # 子序列递归拆分再递归合并  分治


def merge(left, right):
    result = []
    while left and right:   # 这边是判断只要存在子序列，就判断填充进result中
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))   # 将左序列剩余元素填充进result中
    while right:
        result.append(right.pop(0))  # 将右序列剩余元素填充进result中
    return result

# print(mergeSort(arr))