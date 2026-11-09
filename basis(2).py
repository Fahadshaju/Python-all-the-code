class calculator:
    
    def __init__(self,n):
        self.n=n
    def square(self):
        print(self.n*self.n)
    def cube(self):
        print(self.n*self.n*self.n)
    def squareroot(self):
        print(self.n**(1/2))
        
        
s1=calculator(4)
s1.square()
s1.cube()
s1.squareroot()

        