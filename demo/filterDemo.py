# 回数是指从左向右读和从右向左读都是一样的数，
# 例如12321，909。请利用filter()筛选出回数：

def is_palindrome(n):
    str_n = str(n)
    str_p = str_n[::-1]
    if str_n == str_p:
        return True
    else:
        return False
if __name__ == '__main__':
    outlist = filter(is_palindrome,range(1,100))
    print(list(outlist))
