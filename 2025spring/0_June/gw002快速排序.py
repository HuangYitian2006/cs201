sort = None


def quickSort(a, s, e):
    if s >= e:  # 递归终止条件：当子数组长度为0或1时无需排序
        return
    i, j = s, e  # 初始化双指针i（左）和j（右）
    while i != j:
        # 从右向左找第一个小于基准值a[i]的元素
        while i < j and a[i] <= a[j]:
            j -= 1
        a[i], a[j] = a[j], a[i]  # 交换

        # 从左向右找第一个大于基准值a[j]的元素
        while i < j and a[i] <= a[j]:
            i += 1
        a[i], a[j] = a[j], a[i]  # 交换

    # 递归排序左右子数组（此时i=j是基准值的最终位置）
    quickSort(a, s, i - 1)
    quickSort(a, i + 1, e)


n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
quickSort(a, 0, len(a) - 1)
for i in a:
    print(i)