# 快速排序：以第一个值为基准，比基准小的数放到左边列表，比基准大的数放到右边列表，与基准相同的数放到基准列表，继续对左边列表和右边列表递归快速排序
def quick_sort(list):
    less = []
    pivotList = []
    more = []
    # 递归出口
    if len(list) <= 1:
        return list
    else:
        # 将第一个值做为基准
        pivot = list[0]
        for i in list:
            # 将比基准小的值放到less数列
            if i < pivot:
                less.append(i)
            # 将比基准大的值放到more数列
            elif i > pivot:
                more.append(i)
            # 将和基准相同的值保存在基准数列
            else:
                pivotList.append(i)
        # 对less数列和more数列继续进行排序
        less = quick_sort(less)
        more = quick_sort(more)
        return less + pivotList + more


def qsort(arr):
    # 简写√
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x < pivot]
        greater = [x for x in arr[1:] if x >= pivot]
        return qsort(less) + [pivot] + qsort(greater)


# 一行
# def qs(xs): return ((len(xs) <= 1 and [xs]) or [qs(
#     [x for x in xs[1:] if x < xs[0]]) + [xs[0]] + qs([x for x in xs[1:] if x >= xs[0]])])[0]


test = [90, 41, 22, 38, 13, 77, 29, 32, 62]
# quick_sort(test)
print(quick_sort(test))
