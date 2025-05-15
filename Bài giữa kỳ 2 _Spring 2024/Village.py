class Village:
    """
    Lớp mô tả 1 phường thuộc thành phố Hà Nội bao gồm các thông tin sau:
    name :(str) tên phường
    vid:(str) mã phường có dạng A-12345 trong đó ký tự đầu tiên đại diện cho xếp hạng của phường
    trong thành phố.
    A : phường loại 1
    B : phường loại 2
    ...

    town:(str) quận mà phường đó trực thuộc.
    student:(dict) một từ điển chứa năm và số lượng học sinh thi vào cấp 3 của năm đó.
    {key : int, value : int}
    Vd: {2018 : 7000, 2019 : 8000, 2020 : 9000}
    """

    def __init__(self, name, vid, town):
        self.name = name
        self.vid = vid
        self.town = town
        self.student = dict()

    def __str__(self):
        """
        Hàm in thông tin về Village sinh viên không cần làm gì hàm này.
        """
        return '{name:%s, vid:%s, town:%s}' % (self.name, self.vid, self.town)

    def get_rank(self):
        """
        Hàm trả về xếp hạng (int) của phường dựa vào vid.
        vid bắt đầu bằng A : phường loại 1
        vid bắt đầu bằng B : phường loại 2
        vid bắt đầu bằng C : phường loại 3
        vid bắt đầu bằng D : phường loại 4
        """
        if self.vid[0] == 'A':
            return 1
        elif self.vid[0] == 'B':
            return 2
        elif self.vid[0] == 'C':
            return 3
        elif self.vid[0] == 'D':
            return 4
        else:
            return -1

    def get_max_change(self):
        """
        Hàm trả về một tuple gồm 2 phần tử
        phần tử đầu tiên là năm có số lượng tăng thêm thí sinh thi vào cấp 3 nhiều nhất
        phần tử thứ 2 là số lượng tăng thêm tương ứng:

        Ví dụ: {2018 : 7000, 2019 : 7200, 2020 : 8000}	 	  	      	   	      	     	   	       	 	
        Output: (2020, 800)
        Do năm 2020 có thêm 800 thí sinh tăng thêm nhiều nhất so với 2019 (tăng 200)
        Nếu có 2 năm cùng số thí sinh tăng thêm nhiều nhất thì lấy năm đầu tiên đạt giá trị lớn nhất.
        """
        years = list(self.student.keys())
        years.sort()
        max_change = 0
        max_year = 0
        for i in range(1, len(years)):
            change = self.student[years[i]] - self.student[years[i - 1]]
            if change > max_change:
                max_change = change
                max_year = years[i]
        return max_year, max_change
