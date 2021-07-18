class Solutation():
    # def aa(self,lis,tar):
    #     n = len(lis)
    #     mid = n //2
    #     if n>0:
    #         if lis[mid] > tar:
    #             return self.aa(lis[:mid],tar)
    #         elif lis[mid] < tar:
    #             return self.aa(lis[mid+1:],tar)
    #         elif lis[mid] == tar:
    #             return True
    #     return False






    def aa(self,lis,tar):
        n = len(lis)
        mid = n//2
        if n >0:
            if tar == lis[mid]:
                return True
            elif tar < lis[mid]:
                return self.aa(lis[:mid],tar)
            elif tar >lis[mid]:
                return self.aa(lis[mid+1:],tar)
        return False

if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,8]
    tar = 4
    s = Solutation()
    print(s.aa(a,tar))
