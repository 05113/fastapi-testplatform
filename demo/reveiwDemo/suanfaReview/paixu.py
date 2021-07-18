def maopaopaixu(l):
    for item in range(len(l)):
        for j in range(len(l) - item-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return l

def xuanzepaixu(l):
    for item in range(len(l)):
        for j in range(item,len(l)):
            if l[item] > l[j]:
                l[item] ,l[j] = l[j],l[item]
    return l
def charupaixu(l):
    for item in range(len(l)):
        value = l[item]
        for j in range(item-1,-1,-1):
            if value < l[j]:
                l[j],l[j+1] = l[j+1],l[j]
    return l
def kuaisupaixu():

    def kp(li,start , end):
        if start >= end:
            return
        left = start
        right = end
        mid = li[left]
        while left != right:
            while right>left and li[right] >= mid:
                right -= 1
            li[left] = li[right]
            while right > left and li[left] < mid:
                left += 1
            li[right] = li[left]
        li[left] = mid
        kp(li,start,left-1)
        kp(li,left+1,end)
    data_test = [10, 23, 1, 53, 654, 54, 16, 646, 65, 3155, 546, 31]
    kp(data_test, 0, len(data_test) - 1)
    print(data_test)

def kuaipai():
    def sort(li,start,end):
        if start >= end:
            return
        left = start
        right = end
        mid = li[left]
        while left!=right:
            while left<right and li[right]>=mid:
                right -= 1
            li[left] = li[right]
            while left<right and li[left] < mid:
                left += 1
            li[right] = li[left]
        li[left] = mid

        sort(li,start,left-1)
        sort(li,left+1,end)
    data_test = [10, 23, 1, 53, 654, 54, 16, 646, 65, 3155, 546, 31]
    sort(data_test, 0, len(data_test) - 1)
    print('aaa',data_test)







if __name__ == '__main__':
    data_test = [10, 23, 1, 53, 654, 54, 16, 646, 65, 3155, 546, 31]
    print(maopaopaixu(data_test))
    print(xuanzepaixu(data_test))
    print(charupaixu(data_test))
    kuaisupaixu()
    kuaipai()

