class Student:

    def __init__(self,name,mark):

        self.name=name

        self.mark=mark

    def display(self):

        print(self.name)

        print(self.mark)

s1=Student("Fahad",98)

s1.display()