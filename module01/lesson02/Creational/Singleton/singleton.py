class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance


class InheritSingleton(Singleton):
    pass


# Промблеа зі спадковістю стандартного одинака(Singleton)
sg1 = Singleton()
sg2 = Singleton()
sg3 = Singleton()
sg4 = Singleton()
sg5 = Singleton()
sg6 = Singleton()


inhsg = InheritSingleton()
print(sg1 == sg2)
print(id(sg1), id(sg6))

print(sg1 == inhsg)




# # Переход к Meta для избавления (наследуемый не является тем же экземпляром)
# class MetaSingleton(type):
#     __instance = {}

#     def __call__(cls, *args, **kwargs):
#         if cls not in cls.__instance:
#             cls.__instance[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
#         return cls.__instance[cls]


# class InheritMetaSingleton(metaclass=MetaSingleton):
#     pass


# class InheritInheritMetaSingleton(InheritSingleton):
#     pass


# sg1 = InheritMetaSingleton()
# sg2 = InheritMetaSingleton()
# inhsg = InheritInheritMetaSingleton()
# print(sg1 == sg2)
# print(sg1 == inhsg)
