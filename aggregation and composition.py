

# This shows how the composition works
class Composition:
    # We have __Other class inside the Composition class
    class __Other:
        def __init__(self, string):
            self.string = string

        def retrieve_string(self):
            return self.string

    # And we are creating instance of __Other class inside too
    def result(self):
        return self.__Other('Hello').retrieve_string() + ' world!'


# Check
composition = Composition()
print(composition.result())  # Hello world!

# So, When we create instances of other classes in our main class
# This is called composition
# Another example of this is below


# First, let's create Other class
class Other:
    def __init__(self, string):
        self.string = string

    def retrieve_string(self):
        return self.string


# Note, we create an instance of Other class inside the Composition class
# It is important!
# Because it is the main difference between composition and aggregation
class Composition:
    def __init__(self, string):
        self.other_class = Other(string)

    def result(self):
        return self.other_class.retrieve_string() + ' world!'


composition = Composition('Hello')
print(composition.result())  # Hello world!


# The code below shows how aggregation works
class Aggregation:
    def __init__(self, other_class):
        # Here you can see the difference from the composition
        self.other_class = other_class

    def result(self):
        return "Hello " + self.other_class.retrieve_string() + "!"


# We create the instance of the Other class outside the class Aggregation
other = Other("world")
# and pass the already created instance to the Aggregation class constructor
aggregation = Aggregation(other)
print(aggregation.result())  # Hello world!

# So, aggregation is when we use in our main class
# instances of other classes that are created and exist outside our main class
