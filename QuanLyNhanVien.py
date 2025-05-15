
class Employee:

    def __init__(self, eid, name, year, basicSalary):
        self.eid = eid
        self.name = name
        self.year = year
        self.basicSalary = basicSalary

    def getSalary(self):
        return self.basicSalary


class Manager(Employee):

    # Nạp chồng phương thức  tính lương
    def getSalary(self):
        return 1.25 * self.basicSalary


class DataScientist(Employee):

    # Hàm dựng thêm 1 đối project là số dự án  làm trong tháng
    def __init__(self, eid, name, year, basicSalary, project):
        super().__init__(eid, name, year, basicSalary)
        self.project = project

    # Nạp chồng phương thức tính lương
    def getSalary(self):
        return 1.2 * self.basicSalary + 1500 * self.project


class Developer(DataScientist):

    #Nạp chồng phương thức tính lương
    def getSalary(self):
        return self.basicSalary + 1000 * self.project


def loadEmploysFromFile(filename):
    '''
    Phương thức đọc danh sách các nhân viên từ filename, mỗi thông tin của nhân viên lưu trên từng dòng theo thứ tự sau:
    Mã nhân viên (xâu)
    Họ tên (xâu)
    Năm sinh (số nguyên)
    Mức lương cơ bản (số thực)
    Số dự án (số nguyên) (chỉ DataScientist và Developer có dòng này)


    Chú ý:
    - Nếu Mã nhân viên bắt đầu bằng E thì  là nhân viên bình thường Employee
    - Nếu Mã nhân viên bắt đầu bằng M thì  là Quản lý Manager
    - Nếu Mã nhân viên bắt đầu bằng DS thì là nhà phân tích dữ liệu DataScientist
    - Nếu Mã nhân viên bắt đầu bằng DV thì là lập trình viên Developer

    Các nhân viên được đưa lần lượt vào danh sách employees, hàm sẽ trả về danh sách này.

    '''

    employees = []

    file = open(filename, "rt", encoding="utf-8")

    next = True
    while next:

        try:
            eid = file.readline().strip()
            name = file.readline().strip()
            year = int(file.readline().strip())
            salary = float(file.readline().strip())
            if eid.startswith("E"):
                e = Employee(eid, name, year, salary)
            elif eid.startswith("M"):
                e = Manager(eid, name, year, salary)
            elif eid.startswith("DS"):
                e = DataScientist(eid, name, year, salary, int(file.readline().strip()))
            else:
                e = Developer(eid, name, year, salary, int(file.readline().strip()))

            employees.append(e)
        except:
            next = False

    return employees





