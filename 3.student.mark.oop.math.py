import math
import numpy as np
import curses

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
            else: 
                return None
    

    def inputmark(self):
        courseid=input("nhap ID mon muon nhap diem: ")
        c=self.findc(courseid)
        if c == None: 
            print("khong co mon nay!") 
            return
        for s in self.__students:
            print(f"nhap diem cua sv {s}")
            mark=float(input())
            credit=int(input())
            s.addmark(courseid, mark, credit)
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
    def sort(self):
        self.__students.sort(key=lambda s: s.calculategpa(),reverse=True)

    


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
        self.marks = np.array([])
        self.credits = np.array([])
    def getname(self):
        return self.__name
    def getid(self):
        return self.__sid
    def addmark(self, mark, credit):
        mark = math.floor(mark*10)/10
        self.marks = np.append(self.marks, mark)
        self.credits = np.append(self.credits, credit)
    def calculategpa(self):
        if self.credits.sum() == 0:
            return 0.0
        return round(np.dot(self.marks, self.credits)/self.credits.sum(),2)
    def __str__(self):
        return f"Name student: {self.__name}, ID: {self.__sid}"
    
def main():
        room=classroom()
        while True:
            print("nhap sv - chon 1")
            print("nhap mon hoc - chon 2")
            print("nhap diem - chon 3")
            print("ds sv - chon 4")
            print("ds mon hoc - chon 5")
            print("ds diem sv - chon 6")
            print("thoat - chon 7")
            chon=int(input("lua chon:"))
            match chon:
                case 1: classroom.inputsv()
                case 2: classroom.inputcourse()
                case 3: classroom.inputmark()
                case 4: classroom.list_students()
                case 5: classroom.list_courses()
                case 6: 
                    classroom.sor()
                    classroom.list_marks()
                case 7: break
                case _: print("khong hop le")       