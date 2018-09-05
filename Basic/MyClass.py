class MyClass:
    """Doc information for MyClass"""
    i = 12345

    def f(self):
        return 'Hello world'

print(MyClass)
print(MyClass.__doc__)
print(MyClass.f(MyClass))
print(MyClass.i)
