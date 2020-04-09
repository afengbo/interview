# 实现一个二分查找
# 输入: 一个顺序list
# 输出: 待查找的元素的位置


def binarySearch(alist, element):
    first = 0
    last = len(alist) - 1

    while first <= last:
        mid = (first + last) // 2
        # print(mid)
        if alist[mid] > element:
            last = mid - 1
        elif alist[mid] < element:
            first = mid + 1
        else:
            return mid + 1
    return None


test = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarySearch(test, 17))