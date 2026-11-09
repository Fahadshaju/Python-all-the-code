#v INHERTANCE

class father:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"My father name is: {name}")
        print(f"His age is:{age}")
        
class mother:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"My mother name is:{name}")
        print(f"Her  age is:{age}")


    
class son(father,mother):
    pass
    
f=father("shajahan",49)
m=mother("faritha",47)
s=son()


print(s.name,s.age)

    

    