students=[]
courses=[]
marks={}
def nhapsv():
    n=int(input("nhap sl sv: "))
    for _ in range(n):
        name=input("name: ")
        svid=input("id sv: ")
        students.append({"name": name, "svid":svid})
def monhoc():
    n=int(input("nhap so mon hoc: "))
    for _ in range(n):
        name=input("ten mon: ")
        cid=input("id mon hoc:")
        courses.append({"name":name, "cid":cid})
def diem():
    idcourse=input("nhap id mon hoc muon nhap diem: ")
    listid=[]
    for c in courses:
        listid.append(c["cid"])
    if idcourse not in listid:
        print("mon hoc ko ton tai")
        return
    if idcourse not in marks:
        marks[idcourse]={}
        
    print("nhap diem:")
    for s in students:
        m= float(input(f"diem cua {s['name']} id {s['svid']}"))
        marks[idcourse][s["svid"]]=m
def hienthi():
    for s in students:
        print(f"Tensv: {s['name']} id:{s['svid']}")
def danhsachmonhoc():
    for c in courses:
        print(f"mon hoc: {c['name']} id: {c['cid']}")
def dsdiem():
    d=input("nhap id mon muon xem: ")
    if d not in marks:
        print("ko co mon hoc nay")
        return
    for s in students:
        mark=marks.get(d,{}).get(s["svid"])
        if mark is None: 
            print(f"sv {s['name']} id {s['svid']} chua co diem")
            
        else: print(f"sv {s['name']} id {s['svid']} duoc {mark} diem")
def main():
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
            case 1: nhapsv()
            case 2: monhoc()
            case 3: diem()
            case 4: hienthi()
            case 5: danhsachmonhoc()
            case 6: dsdiem()
            case 7: break
            case _: print("khong hop le")
main()
