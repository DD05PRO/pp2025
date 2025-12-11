class classroom:
    def __init__(self):
        self.__students=[]
        self.__courses=[]
    def inputsv(self):
        name=input("Nhap ten sv: ")
        sid=input("nhap ID sv: ")
        self.__students.append(student(name,sid))
    def inputcourse(self):
        name=input("nhap mon hoc: ")
        cid=input("nhap ID mon hoc: ")
        self.__courses.append(course(name, cid))
    def findc(self,cid):
        for c in self.__courses:
            if c.getcid()==cid: 
                return c
            else: return None

    def inputmark(self):
        courseid=input("nhap ID mon muon nhap diem: ")
        c=self.findc(courseid)
        if c == None: 
            print("khong co mon nay!") 
            return
        for s in self.__students:
            print(f"nhap diem cua sv {s}")
            mark=float(input())
            student.set_mark(courseid, mark)
    def list_students(self):
        for s in self.__students:
            print(s)
    def list_courses(self):
        for c in self.__courses:
            print(c)
    def list_marks(self, courseid):
        for s in self.__students:
            mark = s.getmark(courseid)
            if mark is not None:
                print(f"{s.get_name()}: {mark}")
            else:
                print(f"{s.get_name()}: chua co diem")



class course:
    def __init__(self, name, cid):
        self.__name=name
        self.__cid=cid
    def getname(self):
        return self.__name
    def getcid(self):
        return self.__cid
    def __str__(self):
        return f"Name course: {self.__name}, ID: {self.__cid}"



class student:
    def __init__(self, name, sid):
        self.__name=name
        self.__sid=sid
        self.__marks={}
    def getname(self):
        return self.__name
    def getid(self):
        return self.__sid
    def setmark(self, cid, mark):
        self.__marks[cid]=mark
    def getmark(self,cid):
        return self.__marks.get(cid)
    def __str__(self):
        return f"Name student: {self.__name}, ID: {self.__sid}"