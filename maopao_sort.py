# 冒泡排序：
# 不断将大的数字往后移


def bubble_sort(nums):
    for i in range(len(nums) - 1):
        # 改进后的冒泡，设置一个交换标志位，如果第一次内循环完成后没有任何元素发生改变，则直接返回原list
        ex_flag = False
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                ex_flag = True
        if not ex_flag:
            return nums  # 这里代表计算机偷懒成功
    return nums  # 这里代表计算机没有偷懒成功


my_list = [2, 32, 52, 24, 26, 21, 52, 8, 93]
print(bubble_sort(my_list))
# print(my_list)
