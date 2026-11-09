class company:
    company="Google"
    def __init__(self,name,salary,domain):
        self.name=name
        self.salary=salary
        self.domain=domain
        
s1=company("fahad",120000,"data_scientist")
s2=company("arun",180000,"database" )

print(s1.name,s1.salary,s1.domain,s1.company)
print(s2.name,s2.salary,s2.domain,s2.company)