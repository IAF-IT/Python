class Users():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print("Name :" + self.first_name + " " + self.last_name )
        print("Age :" + str(self.age))



myUser = Users("Igor", "Fartusov", 26)
myUser.describe_user()