from Village import Village

def read_village_from_file(fileName):
    """
    Hàm đọc tệp dữ liệu về phường. Hàm này thực hiện đọc dữ liệu từ các phường
    từ tệp fileName sau đó tạo ra các đối tượng Village tương ứng và lưu vào 1 danh
    sách, sau khi kết thúc việc đọc dữ liệu, hàm này trả lại danh sách các phường
    đã tạo được.

    dữ liệu trong tệp fileName được lưu dưới dạng csv,
    dòng đầu tiên là tên các thuộc tính của phường: vid,name,town
    các dòng tiếp theo, mỗi dòng chứa thông tin của 1 phường, mỗi thông tin cách nhau bởi 1 dấu phẩy ,
    Ví dụ:
    vid,name,town
    D-00001,Phúc Xá,Ba Đình
    B-00004,Trúc Bạch,Ba Đình
    D-00006,Vĩnh Phúc,Ba Đình
    """
    vill =[]
    file = open(fileName , 'rt', encoding='utf-8')

    lines = file.readlines()[1:]

    for line in lines:
        va = line.strip().split(',')
        vill.append(Village(va[1], va[0], va[2]))

    file.close()
    return vill

def read_village_student_from_file(fileName, village_list):

    """
    Hàm thực hiện việc đọc file số lượng thí sinh thi vào cấp 3 của mỗi phường để bổ sung thêm thông tin
    vào thuộc tính student của mỗi Village trong village_list,
    Nhiệm vụ của hàm này là đọc dữ liệu số lượng thí sinh thi vào cấp 3 theo năm và ghi vào thuộc tính student
    của phường đó. Chú ý là việc thêm thông tin cần theo đúng mã phường (vid) của phường đó.

    fileName chứa thông tin về số lượng thí sinh thi vào cấp 3 theo từng năm
    được lưu dưới dạng csv.
    Dòng đầu tiên là tên các thuộc tính của dữ liệu: vid,2018,2019,2020,2021,2022,2023 (mã phường và các năm khảo sát)
    dữ liệu của mỗi phường được lưu trên 1 dòng bao gồm mã phường và số lượng thí sinh tương ứng với năm đó.

    Ví dụ về file:

    vid,2018,2019,2020,2021,2022,2023
    D-00001,7408,7554,7674,7775,7875,7969
    B-00004,6758,6883,6986,7074,7148,7277
    D-00006,7000,7114,7197,7331,7470,7566
    D-00007,7377,7492,7592,7710,7843,7942
    """
    file = open(fileName, 'rt', encoding='utf-8')

    lines = file.readlines()[1:]

    for line in lines:
        va = line.strip().split(',')
        vid = va[0]
        for village in village_list:
            if village.vid == vid:
                for i in range(1, len(va)):
                    year = 2017 + i
                    village.student[year] = int(va[i])
                break

    file.close()


def get_Hanoi_student_change(village_list):
    """
    Hàm thực hiện trả về danh sách các năm (int)được sắp xếp tăng dần theo
    số lượng thí sinh thi vào cấp 3 TĂNG THÊM mỗi năm trên toàn thành phố Hà Nội.
    output: [2021, 2023, 2020, 2019, 2022]
    """

    student_change = {}	 	  	      	   	      	     	   	       	 	
    for village in village_list:
        years = list(village.student.keys())
        years.sort()
        for i in range(1, len(years)):
            change = village.student[years[i]] - village.student[years[i - 1]]
            if years[i] not in student_change:
                student_change[years[i]] = 0
            student_change[years[i]] += change

    sorted_years = sorted(student_change.items(), key=lambda x: x[1], reverse=False)
    return [year[0] for year in sorted_years]

def get_top_village_by_year(village_list, rank, year):

    """
    Hàm trả về 1 danh sách tên phường với xếp hạng ( = rank)
    và có số lượng thí sinh trong năm (year)
    lớn hơn giá trị trung bình của tất cả số thí sinh của thành phố Hà Nội trong năm đó
    Danh sách được sắp sếp theo số lượng thí sinh.

    Ví dụ: rank = 2, year = 2018
    Tìm tất cả tên phường trong đó phường là phường loại 2 có số thí sinh thi vào cấp 3
    năm 2018 lớn hơn trung bình số thí sinh thi vào cấp 3 năm 2018 trên toàn thành phố Hà Nội.
    output: ['Hàng Đào', 'Cống Vị', 'Phúc Tân', 'Cửa Đông', 'Phúc Xá', 'Phú Thượng', 'Điện Biên', 'Hàng Bài', 'Phan Chu Trinh']
    """

    total_by_year = {}

    # Tính tổng số học sinh mỗi năm
    for village in village_list:
        for year1, count in village.student.items():
            if year1 not in total_by_year:
                total_by_year[year1] = 0
            total_by_year[year1] += count

    for year2 in total_by_year:
        total_by_year[year2] /= len(village_list)
    
    dict = {}	 	  	      	   	      	     	   	       	 	
    for village in village_list:
        if village.get_rank() != rank:
            continue
        if village.student[year] > total_by_year[year]:
            dict[village.name] = village.student[year]

    result = sorted(dict.items(), key= lambda x : x[1])
    result = [i[0] for i in result]
    return result


def sorted_town_by_avg_student(village_list):

    """
    Hàm trả về một danh sách các quận (town) được xắp sếp tăng dần
    theo số lượng thí sinh thi cấp 3 trung bình của các phường trong quận đó.
    Giá trị trung bình được tính trên tất cả các năm cho tất cả các phường thuộc quận đó

    output: ['Ba Đình','Cầu Giấy','Hoàn Kiếm','Long Biên','Tây Hồ']
    """
    town_avg = {}
    for village in village_list:
        if village.town not in town_avg:
            town_avg[village.town] = []
        town_avg[village.town].append(village)

    avg_list = []
    for town, villages in town_avg.items():
        total_students = 0
        count = 0
        for village in villages:
            for year, students in village.student.items():
                total_students += students
                count += 1
        avg_students = total_students / count if count > 0 else 0
        avg_list.append((town, avg_students))

    sorted_town = sorted(avg_list, key=lambda x: x[1])
    return [town[0] for town in sorted_town]
	 	  	      	   	      	     	   	       	 	
