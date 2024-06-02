class person:
    def __init__(self,name,a_name):
        self.firstname=name
        self.lastname=a_name
        
    def dname(self):
        print(self.firstname,self.lastname)
    
    
x= person('deepak','dfdfd')
x.dname()