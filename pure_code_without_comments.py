class Composition:
    class __Other:
        def __init__(self, string):
            self.string = string

        def retrieve_string(self):
            return self.string

    def result(self):
        return self.__Other('Hello').retrieve_string() + ' world!'


composition = Composition()
print(composition.result())


class Other:
    def __init__(self, string):
        self.string = string

    def retrieve_string(self):
        return self.string


class Composition:
    def __init__(self, string):
        self.other_class = Other(string)

    def result(self):
        return self.other_class.retrieve_string() + ' world!'


composition = Composition('Hello')
print(composition.result())


class Aggregation:
    def __init__(self, other_class):
        self.other_class = other_class

    def result(self):
        return "Hello " + self.other_class.retrieve_string() + "!"


other = Other("world")
aggregation = Aggregation(other)
print(aggregation.result())
