class Driver:
    """
    Lớp mô tả một lái xe bao gồm các thông tin sau:
    name : (str) tên của lái xe
    did : (str) id của lái xe có dạng A12345
    years: (int) số năm kinh nghiệm lái xe
    """
    def __init__(self, name, did, years) -> None:
        self.name = name
        self.did = did
        self.years = years
        self.set_client()
        self.set_salary(self.get_basic_salary())

    def set_client(self):
        # sinh viên không cần thực hiện gì hàm này.
        """
        client: (str) loại bằng lái của lái xe. 
        client nằm một trong 5 loại sau A B C D E
        bằng loại A: dành cho xe <= 4 chỗ.
        bằng loại B: dành cho xe <= 7 chỗ.
        bằng loại C: dành cho xe <= 16 chỗ.
        bằng loại D: dành cho xe <= 29 chỗ.
        bằng loại E: dành cho xe <= 49 chỗ.
        """
        self.__client = self.did[0]
    
    def get_client(self):
        # Hàm trả về thông tin loại bằng của lái xe
        # Sinh viên không cần thực hiện hàm này.
        return self.__client

    def set_salary(self, salary):
        # Sinh viên không cần thực hiện hàm này.
        self.__salary = salary
        
    def get_basic_salary(self):
        """
        Phương thức này trả về mức lương cơ bản của một lái xe.
        Lương cơ bản của tất cả lái xe là 3_000_000
        Mức hỗ trợ theo thâm niên và kỹ năng như sau:
        Với lái xe có bằng lái xe hạng C, D, E thì lương được cộng thêm lần lượt 
        500_000, 700_000, 2_000_000,
        Với lái xe có <= 5 năm kinh nghiệm thì được tăng thêm 200_000 cho mỗi năm.
        Với lái xe có > 5 năm kinh nghiệm thì được tăng thêm 600_000 cho mỗi năm tiếp theo.
        Ví dụ: lái xe có 7 năm kinh nghiệm sẽ có mức tăng thêm là 2_200_000
        
        Vd: {name : Tô Hải Anh, did : D38834, years : 4} => basic_salary = 4_500_000
        
        Chú ý, dấu gạch dưới trong các số chỉ để giúp việc đọc dễ hơn, khi làm bài sinh viên sử dụng
        các giá trị số như bình thường, ví dụ 3000000
        """
        base_salary = 3_000_000
        license_bonus = 0
        
        # Thưởng theo loại bằng lái
        client = self.get_client()
        if client == 'C':
            license_bonus = 500_000
        elif client == 'D':
            license_bonus = 700_000
        elif client == 'E':
            license_bonus = 2_000_000
        
        # Tính tiền thưởng theo thâm niên
        years = self.years
        seniority_bonus = 0
        if years <= 5:
            seniority_bonus = years * 200_000
        else:
            seniority_bonus = 5 * 200_000 + (years - 5) * 600_000
        
        return base_salary + license_bonus + seniority_bonus
    
    
    def get_salary(self):
        # sinh viên không cần thực hiện gì hàm này
        return self.__salary
 
   
    def __str__(self) -> str:
        # hàm in ra đối tượng Driver. Sinh viên không cần thực hiện gì hàm này.
        return f'{{name: {self.name:s}, did: {self.did:s}, years: {self.years:d}}}'

class Ticket:
    
    """
    Lớp mô tả một hóa đơn vận tải khách bao gồm thông tin sau:
    tid: (int) id của hóa đơn
    date: (int) [1-30] ngày lập hóa đơn trong tháng 
    start_time: (int) [0-23] thời gian bắt đầu đón khách
    end_time: (int) [0-23] thời gian trả khách
    start_time, end_time được hiểu là giờ trong ngày.
    num_seats : (int) số ghế mà xe có
        num_seats nằm trong một trong các loại sau: 4 7 16 29 49
    num_customers: (int) số lượng khách
    vote: (int) [1-5] đánh giá của khách hàng về chuyến đi
    driver: (Driver) đối tượng thuộc lớp Driver, cung cấp thông tin về tài xế
    thực hiện chuyến xe.
    """
    
    
    def __init__(self, tid, date, stime, etime,nseats, ncustomers, vote, driver) -> None:
        self.tid = tid
        self.date = date
        self.start_time = stime
        self.end_time = etime
        self.num_seats = nseats
        self.num_customers = ncustomers    
        self.vote = vote
        self.driver = driver
        self.reward()
    
    def reward(self):
        """
        Hàm tính tiền thưởng/phạt cho lái xe sau mỗi hóa đơn.
        Với mỗi hóa đơn có bình chọn (vote) 5 sao. Thì lái xe sẽ
        được thưởng 200_000 cho hóa đơn đó.
        
        Nếu thời gian di chuyển (end_time - start_time) > 9
        thì lái xe được hỗ trợ 100_000 / mỗi giờ tăng thêm.
        
        Nếu tài sế bị bình chọn (vote) <= 2 sao. Lái xe sẽ bị phạt 300_000
        
        Tiền thưởng/phạt sẽ được cộng/trừ trực tiếp vào lương của tài xế
        Gợi ý: dùng hàm set_salary() để cập nhật lương
        dùng hàm get_salary() để lấy mức lương hiện tại (chưa tính thưởng/phạt)
        """
        current_salary = self.driver.get_salary()
        
        if self.vote == 5:
            current_salary += 200_000
        
        duration = self.end_time - self.start_time
        if duration > 9:
            extra_hours = duration - 9
            current_salary += extra_hours * 100_000
        
        if self.vote <= 2:
            current_salary -= 300_000
        
        self.driver.set_salary(current_salary)
        
        
    def __str__(self) -> str:
        return f"{{tid: {self.tid:d}, did: {self.driver.did:s}, dname: {self.driver.name:s}," \
               f" date: {self.date:d}, stime: {self.start_time:d}, etime: {self.end_time:d}," \
               f"num_seats: {self.num_seats:d}, num_cus: {self.num_customers:d}, vote: {self.vote:d}}}"

             	 	  	      	   	      	     	   	       	 	
