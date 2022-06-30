# class A:
#
#     def method(self):
#         print("Its method in class A")
#
#
# class B:
#
#     def method_b(self):
#         print("Its method in class B")
#
#
# class C(A,B):
#     pass
#
#
# exm_c = C() # Instance C
#
# print(exm_c)



class A:
    def method_a(self):
        print("Its method in class A")

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

exm_d = D()
exm_d.method_a()

print(D.mro())
