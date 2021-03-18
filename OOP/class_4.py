class Math:

    @staticmethod
    # Do not put self or cls
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10


print(Math.add5(5))
print(Math.add10(42))
