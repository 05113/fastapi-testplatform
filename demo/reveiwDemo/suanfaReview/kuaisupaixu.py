class Soluation():
    def sort1(self,lit,start,end):
        if start > end:
            return
        left = start
        right = end
        mid = lit[left]
        while left<right:
            while left<right and lit[right] >= mid:
                right -= 1
            lit[left] = lit[right]
            while left<right and lit[left] < mid:
                left += 1
            lit[right] = lit[left]
        lit[left] = mid
        self.sort1(lit,start,left-1)
        self.sort1(lit,left+1,end)


if __name__ == '__main__':
    s = Soluation()
    data_test = [10, 23, 1, 53, 654, 54, 16, 646, 65, 3155, 546, 31]
    s.sort1(data_test,0,len(data_test)-1)
    print(data_test)
