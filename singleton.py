class Singleton:
    _instance=None
    def __new__(cls):
        if cls._instance is None:
            print("Creating the object")
            cls._instance=super().__new__(cls)
        return cls._instance
ob1=Singleton()
ob2=Singleton()
print(ob1)
print(ob2)
print(ob2 is ob1)