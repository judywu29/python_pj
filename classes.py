class Parent(object):
    x = 1
class Child1(Parent):
        pass
class Child2(Parent):
        pass

print(Parent.x, Child1.x, Child2.x)


Child1.x = 2
print(Parent.x, Child1.x, Child2.x)


Parent.x = 3
print(Parent.x, Child1.x, Child2.x)  #3 2 3

# 在 Python 中，类变量在内部是作为字典处理的。如果一个变量的名字没有在当前类的字典中发现，将搜索祖先类（比如父类）直到被引用的变量名被找到（如果这个被引用的变量名既没有在自己所在的类又没有在祖先类中找到，会引发一个 AttributeError 异常 ）
# 如果该值在父类中被改变（例如，我们执行语句 Parent.x = 3），这个改变会影响到任何未重写该值的子类当中的值（在这个示例中被影响的子类是 Child2）。这就是为什么第三个 print 输出是 3 2 3