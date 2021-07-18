# a[2,-1,5,6,-10,2,-3,7]


def function(lists):
    a = []
    b = []
    max_sum = lists[0]
    pre_sum = 0
    for i in lists:
        if pre_sum < 0:
            pre_sum = i
            b = a
            a=[]

        else:
            pre_sum += i
        if pre_sum > max_sum:
            max_sum = pre_sum
            a.append(i)
    return max_sum,a
if __name__ == '__main__':
    lists = [6, -3, 1, -2, 7, -15, 1, 2, 2]
    # lists = [-1,2,3,-5,10,15]
    print(function(lists))
