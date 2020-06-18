
# create class

class Restaurant():
    # create class
    def __init__(self, name, type):
        # initialize attributes name, type
        self.name = name
        self.type = type

    def describe(self):
        print(self.name.title() + " " + self.type.title())

    def open_rest(self):
        print("Restaurant is open ! ")





myRest = Restaurant('Olo', 'Asian')
myRest.describe()
myRest.open_rest()



