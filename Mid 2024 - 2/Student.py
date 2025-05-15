class Student:
    
    """
    Lớp mô tả 1 sinh viên bao gồm các thông tin sau:
    name :(str) tên sinh viên
    sid:(int) mã số sinh viên có định dạng 2000xxxx trong đó 2 mã số đầu
    đại diện cho năm nhập học của sinh viên.
    Sinh viên năm nhất hiện có mssv bắt đầu bằng 2200xxxx
    department:(str) khoa sinh viên đang theo học.
    grade:(dict) một từ điển chứa mã môn học và điểm số tương ứng với môn học đó.
    điểm được chấm theo thang 100.
    """
    
    def __init__(self, name, sid, department):
        self.name = name
        self.sid = sid
        self.department = department
        self.grade = dict()
    
    def __str__(self):
        """
        Hàm in thông tin student sinh viên không cần làm gì hàm này.
        """
        return  '{name:%s, sid:%s, department:%s}'%(self.name, self.sid, self.department)
        
    def get_year(self):
        """
        Hàm trả về sinh viên đang theo học năm thứ mấy.
        sid bắt đầu bằng 2200 : sinh viên năm 1
        sid bắt đầu bằng 2100 : sinh viên năm 2
        ...
        sid bắt đầu bằng 1800: sinh viên năm 5
        """
        # Lấy 4 chữ số đầu của sid (ví dụ 22001234 lấy 2200)
        sid_prefix = str(self.sid)[:4]
        # Lấy số đầu tiên của sid_prefix (ví dụ 2 trong 2200)
        first_digit = int(sid_prefix[0])
        # Lấy số 2 chữ số sau đầu (ví dụ 20 trong 2200)
        year_code = int(sid_prefix[1:3])
        
        # Nếu năm bắt đầu bằng 22 là năm 1, 21 là năm 2, ..., 18 là năm 5
        # Tính năm học theo công thức: 22 - year_code + 1
        # Ví dụ: 2200 -> year_code=20 -> 22 - 20 +1 = 3 (sai) -> cần sửa cách tính
        
        # Theo mô tả, sid bắt đầu bằng 2200 là năm 1
        # Tức 22 tương ứng năm 1, 21 tương ứng năm 2, 20 tương ứng năm 3,...
        # Vậy ta lấy số đầu tiên 2 chữ số -> 22, trừ đi 17 (vì 18 là năm 5)
        
        # Lấy 2 số đầu làm số năm nhập học
        year_prefix = int(sid_prefix[:2])  # lấy 2 số đầu: 22, 21, 20, 19, 18
        
        if 18 <= year_prefix <= 22:
            return 22 - year_prefix + 1
        else:
            return -1
        
    def get_avg_grade(self):
        """
        Hàm trả về điểm trung bình của sinh viên
        """
        if not self.grade:
            return 0.0
        total = sum(self.grade.values())
        count = len(self.grade)
        return total / count
	 	  	      	   	      	     	   	       	 	
