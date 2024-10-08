class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)
        
    def setFname(self):
        return self.firstname
    
    def __str__(self):
        return f"{self.firstname}"

    
#Use the Person class to create an object, and then execute the printname method:

class SinhVien(Person):
    def __init__(self,fname, lname, lop) :
        self.lop = lop
        # self.firstname = fname
        # self.lastname = lname
        super().__init__(fname,lname)
    
        
        
        
if __name__ == "__main__":
    # x = Person("John", "Doe")
    # # x.printname()
    # # x.__str__()

    # print(x)
    sv = SinhVien("Â","ÂVA",10)
    print(sv)
    sv.printname()