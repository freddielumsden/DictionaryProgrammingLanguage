class fdict():  # Felicity style dictionary
    def __init__(self, keys=[], values=[]):
        self.keys = keys
        self.values = values

    def append(self, key, value):
        if key in self.keys:
            del self.values[self.keys.index(key)]
            self.keys.remove(key)
        self.keys.append(key)
        self.values.append(value)

    def get_value(self, key):
        return self.values[self.keys.index(key)]


main = fdict(["print"], ["HELLO"])
print(main.get_value("print"))
