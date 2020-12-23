class A:
    @staticmethod
    def meth(value):
            print(value)
a = A()
a.meth(1)
A.meth('hello')
