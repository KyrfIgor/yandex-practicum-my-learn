MyClass = type('MyClass', (object,), {'test_attr': 15})
print(type(MyClass))

my_class_inst = MyClass()
print(my_class_inst.test_attr)