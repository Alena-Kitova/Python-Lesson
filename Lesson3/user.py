class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def sayfirst_name(self):
        print(self.first_name)

    def saylast_name(self):
        print(self.last_name)

    def sayfirstlast_name(self):
        print(self.first_name, self.last_name)
