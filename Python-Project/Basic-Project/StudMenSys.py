class Classes:

    def __init__(self,sClass):
        self.type = self.Student(sClass)
        self.stdRollNo = sClass+"001"

    def Display(self):
        print("\nYour Roll No : "+self.stdRollNo)

    class Student:

        def __init__(self,sclass):
            name = input("Enter your name : ")
            self.stdName = name
            addr = str(input("Enter your Address : "))
            self.stdAddr = addr
            m_no = str(input("Enter your Mobile no : "))
            self.stdM_No = m_no
            f_name = str(input("Enter your Father name : "))
            self.stdF_Name = f_name
            m_name = str(input("Enter your Mother name : "))
            self.stdM_Name = m_name
            self.stdClass = sclass

if __name__ == "__main__":
    Class = str(input("Which Class you admition : "))
    sclass = Class

    Class = Classes(sclass)

    Class.Display()
    print("Your Name : "+Class.type.stdName)
    print("Your Address : "+Class.type.stdAddr)
    print("Your Mobile No : "+Class.type.stdM_No)
    print("Your Fathers Name : "+Class.type.stdF_Name)
    print("Your Mothers Name : "+Class.type.stdM_Name)
    print("Your Class : "+Class.type.stdClass)


