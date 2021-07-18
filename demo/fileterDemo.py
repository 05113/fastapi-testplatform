'''
filter方法求出列表所有奇数并构造新列表，a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''

def kk(num):
    if num % 2 == 0:
        return False
    else:
        return True
if __name__ == '__main__':
    l = [1,2,3,4,5,6]
    n = filter(kk,l)
    for item in n:
        print(item)