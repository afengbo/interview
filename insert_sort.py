# 插入排序
# 主要思想是每次取一个列表元素与列表中已经排序好的列表段进行比较，然后插入从而得到新的排序好的列表段，最终获得排序好的列表。（debug查看排序步骤）


def insertion_sort(alist):
    for index in range(1, len(alist)):
        current_num = alist[index]
        while index > 0 and current_num < alist[index - 1]:
            alist[index] = alist[index - 1]
            index -= 1
        alist[index] = current_num


test = [90, 41, 22, 38, 13, 77, 29, 32, 62]
insertion_sort(test)
print(test)
