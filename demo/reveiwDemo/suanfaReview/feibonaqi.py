class Solu():
    def fb(self,n):
        res = [1,1]
        a,b =1,1

        for item in range(n):
            a,b = b,a+b
            res.append(b)

        return res
if __name__ == '__main__':
    s = Solu()
    a = s.fb(5)
    print(a)