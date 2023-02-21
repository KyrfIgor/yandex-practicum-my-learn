class MyClass:
    def __new__(cls, *args, **kwargs):
        new_instance = object.__new__(cls)
        print(f"{cls.__name__}: Вызван метод __new__")
        return new_instance

    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2
        print(f"{self.__class__.__name__}: Вызван метод __init__")

    def __del__(self):
        print(f"{self.__class__.__name__}: Вызван метод __del__")

if __name__ == "__main__":
    print("Начало работы программы")

    print("Создаём и инициализируем новый объект")
    obj_inst = MyClass(100, "World")

    print("Вызываем деструктор объекта")
    del obj_inst

    print("Завершение работы программы")