class Test(object):
    d={}
    d[1]='a'
    d[2]='b'
    d[3]='c'
    def remove(self,k):
        if k:
            Test.d.pop(k)
        return Test.d
    def show(self):
        print(Test.d)

print(Test.d)
t=Test()
t.show()            
t1=Test()
t1.remove(1)
t1.show()
t1.remove(3)
t1.show()
t1.remove(2)
t1.show()
t.show()