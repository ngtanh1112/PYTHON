from Student import Student
import csv

def read_student_from_file(studentFile):
    """
    Đọc file csv chứa thông tin sinh viên và tạo danh sách Student.
    """
    student_list = []
    with open(studentFile, encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)  # Bỏ qua dòng tiêu đề
        for row in reader:
            if len(row) < 3:
                continue
            name, sid_str, department = row
            sid = int(sid_str)
            student = Student(name, sid, department)
            student_list.append(student)
    return student_list

def read_grade_from_file(gradeFile, student_list):
    """
    Đọc file điểm và cập nhật vào từ điển grade của từng Student trong student_list.
    """
    # Tạo map mã sinh viên -> đối tượng Student để truy cập nhanh
    sid_to_student = {stu.sid: stu for stu in student_list}
    
    with open(gradeFile, encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        subjects = header[1:]  # danh sách môn học, ví dụ ['CS', 'CV', 'DSA', ...]
        
        for row in reader:
            if len(row) < 2:
                continue
            sid_str = row[0]
            sid = int(sid_str)
            grades = row[1:]
            if sid in sid_to_student:
                grade_dict = {}	 	  	      	   	      	     	   	       	 	
                for subject, grade_str in zip(subjects, grades):
                    try:
                        grade_dict[subject] = int(grade_str)
                    except:
                        grade_dict[subject] = 0
                sid_to_student[sid].grade = grade_dict

def get_best_student_avg_grade(student_list):
    """
    Trả về tuple (tên sinh viên điểm trung bình thấp nhất, tên sinh viên điểm trung bình cao nhất)
    """
    if not student_list:
        return None
    
    student_list = [stu for stu in student_list if stu.grade]
    if not student_list:
        return None
    
    # Tìm sinh viên có điểm trung bình thấp nhất và cao nhất
    min_student = min(student_list, key=lambda x: x.get_avg_grade())
    max_student = max(student_list, key=lambda x: x.get_avg_grade())
    return (min_student.name, max_student.name)

def get_best_student_by_year(student_list, year, class_id):
    """
    Trả về student (đối tượng) có điểm môn class_id cao nhất trong năm học year
    """
    # Lọc sinh viên theo năm học
    filtered_students = [stu for stu in student_list if stu.get_year() == year and class_id in stu.grade]
    if not filtered_students:
        return None
    # Tìm sinh viên có điểm môn class_id cao nhất
    best_student = max(filtered_students, key=lambda x: x.grade[class_id])
    return best_student

def sorted_department_by_avg_student_grade(student_list):
    """
    Trả về danh sách các khoa, được sắp xếp theo điểm trung bình của sinh viên khoa đó (tăng dần)
    """
    # Tạo dict: khoa -> list điểm trung bình của sinh viên
    dept_avg = {}	 	  	      	   	      	     	   	       	 	
    for stu in student_list:
        avg = stu.get_avg_grade()
        if stu.department not in dept_avg:
            dept_avg[stu.department] = []
        dept_avg[stu.department].append(avg)
    
    # Tính trung bình điểm từng khoa
    dept_avg_score = []
    for dept, scores in dept_avg.items():
        if scores:
            avg_score = sum(scores) / len(scores)
        else:
            avg_score = 0
        dept_avg_score.append((dept, avg_score))
    
    # Sắp xếp theo điểm trung bình tăng dần
    dept_avg_score.sort(key=lambda x: x[1])
    
    # Trả về danh sách tên khoa
    return [dept for dept, _ in dept_avg_score]
