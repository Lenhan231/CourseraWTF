class Subject:
        def __init__(self, Name, Code, Course):
            self.code = Code
            self.name = Name
            self.course = Course
        
        def hienthi(self):
            print(f'{self.code}\t{self.name}\t{self.course}')
           

def show(sub):
    order = input("Find by code: ")
    print("Code\tName\tCourse ")
    for i in sub:
        if i.code == order:
            i.hienthi()

def addcode(sub):
    sub.append(Subject(input("Name: "), input("Code: "), input("Course: ")))
    
def deletecode(sub):
    DC = input("Delete code: ")
    for i in sub:
        if i.code == DC:
            sub.remove(i)

def listshow(sub):
    print("List: ")
    print("Code\tName\tCourse ")
    for i in sub:
        i.hienthi()

def main():
    with open("D:\CourseraWTF\DanhSachSinhVien\MonHoc.txt", "r") as mh:
        sub = []
        count = 0
        while True:
            NameSub = mh.readline().strip()
            if NameSub != "":
                sub.append(Subject(NameSub, mh.readline().strip(), mh.readline().strip()))
                count += 1
            else:
                break
        xuly(sub)

def xuly(sub):
    function = ["1. Courses Information", "2. Adding a Course", "3. Deleting a Course", "4. Courses Information Searching", "5. List Show"]
    print("Menu:")
    print('\n'.join(function))
    Case(sub)

def final(sub):
    with open("D:\CourseraWTF\DanhSachSinhVien\DanhSach.txt", "w") as ds:
            ds.write("Code\tName\tCourse\n")
            for i in sub:
                ds.write(f"{i.code}\t{i.name}\t{i.course}\n")

def Case(sub):
    order = input("Press E/e to exit or press number to order: ")
    while order not in 'Ee':
        try:
            order = int(order)
        except:
            Case(sub)
        while order not in [1, 2, 3, 4, 5]:
            try:
                order = int(input("Step: "))
            except ValueError:
                print("Please enter a valid integer.")
        if order == 1:
            show(sub)
        elif order == 2:
            addcode(sub)
        elif order == 3:
            deletecode(sub)
        elif order == 4:
            pass
        elif order == 5:
            listshow(sub)
        print("")
        xuly(sub)
        order = input("Press E/e to exit or press number to order: ")
    final(sub)
    exit()
        

main()
