'''
传入一个list,输出最大连续子数组的和

'''

def zuidalianxu(l):
    maxl = l[0]
    currl = 0
    for item in l:
        if currl <0:
            currl = item
        else:
            currl = currl + item
        if currl > maxl:
            maxl = currl
    return maxl
