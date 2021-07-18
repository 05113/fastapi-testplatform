def moapoDemo(intlist):
    for i in range(len(intlist)):
        for j in range(1,len(intlist) - i):
            if intlist[j-1] > intlist[j]:
                intlist[j-1],intlist[j] = intlist[j] , intlist[j-1]
    return intlist
def xuanzeDemo(intlist):
    for i in range(len(intlist)):
        for j in range(i , len(intlist)):
            if intlist[i] > intlist[j]:
                intlist[i],intlist[j] = intlist[j],intlist[i]
    return intlist
def charupaixu(intl):
    for i in range(1,len(intl)):
        value = intl[i]
        for j in range(i-1,-1,-1):
            if intl[j] < value:
                break
            else:
                intl[j],intl[j+1] = value,intl[j]
    return intl

def guibingpaixu(intlist):
    def merge(left, right):
        i, j = 0, 0
        result = []
        while i < len(left) and j < len(right):  # 比较传入的两个子序列，对两个子序列进行排序
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])  # 将排好序的子序列合并
        result.extend(right[j:])
        return result

    def merge_sort(lst):
        if len(lst) <= 1:
            return lst  # 从递归中返回长度为1的序列

        middle = len(lst) // 2
        left = merge_sort(lst[:middle])  # 通过不断递归，将原始序列拆分成n个小序列
        right = merge_sort(lst[middle:])
        return merge(left, right)
    data_test = [10, 23, 1, 53, 654, 54, 16, 646, 65, 3155, 546, 31]
    print(merge_sort(data_test))
def kuaisupaixu(lit,low,hith):


    pass
def guibingpaixu1():
    def merge_sort(list1):

        if len(list1) < 2:
            return list1
        middle = len(list1) //2

        left = merge_sort(list1[:middle])
        right = merge_sort(list1[middle:])

        return merge(left,right)



    def merge(left,right):
        i ,j = 0,0
        res = []
        while i < len(left) and j < (len(right)):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res.extend(left[i:])
        res.extend(right[j:])
        return res
    data_test = [10, 23, 1, 53, 654, 54, 16, 646, 65, 3155, 546, 31]
    print(merge_sort(data_test))

def charupaixu1(list1):
    for item in range(1,len(list1)):
        value = list1[item]
        for j in range(item-1,-1,-1):
            if list1[j] > value:
                list1[j],list1[j+1] = value,list1[j]
            else:
                break
    return list1

def kuaisupaixu():
    def quick_sort(li, start, end):
        # 分治 一分为二
        # start=end ,证明要处理的数据只有一个
        # start>end ,证明右边没有数据
        if start >= end:
            return
        # 定义两个游标，分别指向0和末尾位置
        left = start
        right = end
        # 把0位置的数据，认为是中间值
        mid = li[left]
        while left != right:
            # 让右边游标往左移动，目的是找到小于mid的值，放到left游标位置
            while left < right and li[right] >= mid:
                right -= 1
            li[left] = li[right]
            # 让左边游标往右移动，目的是找到大于mid的值，放到right游标位置
            while left < right and li[left] < mid:
                left += 1
            li[right] = li[left]
        # while结束后，把mid放到中间位置，left=right
        li[left] = mid
        # 递归处理左边的数据
        quick_sort(li, start, left - 1)
        # 递归处理右边的数据
        quick_sort(li, left + 1, end)


    data_test = [10, 23, 1, 53, 654, 54, 16, 646, 65, 3155, 546, 31]
    da = [3,10,6,1,2]
    quick_sort(da, 0, len(da) - 1)
    print(da)





if __name__ == '__main__':
    data_test = [10, 23, 1, 53, 654, 54, 16, 646, 65, 3155, 546, 31]

    print(moapoDemo(data_test))

    print(xuanzeDemo(data_test))

    guibingpaixu(1)
    guibingpaixu1()

    print(charupaixu1(data_test))

    kuaisupaixu()