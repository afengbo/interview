# 选择排序: 找到最小的数往前扔
def selectionSort(alist):
    for i in range(len(alist) - 1):
        min = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[min]:
                min = j
        alist[i], alist[min] = alist[min], alist[i]
    return alist


test = [90, 41, 22, 38, 13, 77, 29, 32, 62]
print(selectionSort(test))
