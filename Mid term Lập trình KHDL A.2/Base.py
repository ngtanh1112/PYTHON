import csv
from collections import defaultdict

def linear_regression(x, y):
    """
    Tính toán hệ số a và b của phương trình hồi quy y = ax + b.
    """
    n = len(x)
    if n == 0:
        return 0.0, 0.0
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denominator = sum((x[i] - mean_x) ** 2 for i in range(n))
    
    if denominator == 0:
        a = 0.0
    else:
        a = numerator / denominator
    
    b = mean_y - a * mean_x
    
    # Làm tròn đến 5 chữ số thập phân
    a = round(a, 5)
    b = round(b, 5)
    return a, b


def caculate_mse(a, b, x, y):
    """
    Tính MSE cho mô hình y = ax + b.
    """
    n = len(x)
    if n == 0:
        return 0.0
    mse = sum((y[i] - (a * x[i] + b))**2 for i in range(n)) / n
    return mse


def read_bill_from_file(billFile):
    """
    Đọc dữ liệu hóa đơn từ file CSV trả về list các tuple (bill_id, customer_id, res_id, total)
    """
    bill_list = []
    with open(billFile, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Đọc dòng tiêu đề
        for row in reader:
            try:
                bill_id = int(row[0])
                customer_id = int(row[1])
                res_id = int(row[2])
                total = int(row[3])
                bill_list.append((bill_id, customer_id, res_id, total))
            except ValueError:
                print(f"Lỗi chuyển đổi kiểu dữ liệu cho dòng: {row}")
    return bill_list


def sort_restaurance_by_total(billList):
    """
    Trả về danh sách id cửa hàng sắp xếp theo tổng doanh thu tăng dần.
    """
    revenue_by_res = defaultdict(float)
    for _, _, res_id, total in billList:
        revenue_by_res[res_id] += total
    # Sắp xếp theo doanh thu tăng dần, lấy key res_id
    sorted_res = sorted(revenue_by_res.items(), key=lambda x: x[1])
    return [res_id for res_id, _ in sorted_res]


def get_loyal_customer(bill_list):
    """
    Tìm loyal customer: khách hàng chi tiêu ở tất cả cửa hàng và có trung bình chi tiêu cao nhất
    
    Trả về tuple: (customer_id, avg_spending)
    Nếu không có khách hàng nào thỏa mãn trả về (0.0, 0.0)
    """
    customer_bills = {}	 	  	      	   	      	     	   	       	 	
    all_restaurants = set()

    for bill in bill_list:
        customer_id = bill[1]
        res_id = bill[2]
        total = bill[3]
        all_restaurants.add(res_id)
        if customer_id not in customer_bills:
            customer_bills[customer_id] = []
        customer_bills[customer_id].append((res_id, total))

    loyal_customers = {}
    for customer_id, bills in customer_bills.items():
        visited_restaurants = set(res_id for res_id, total in bills)
        if visited_restaurants == all_restaurants and all_restaurants:
            total_spent = sum(total for res_id, total in bills)
            avg_spent = total_spent / len(bills)
            loyal_customers[customer_id] = avg_spent

    if not loyal_customers:
        return 0.0, 0.0

    best_customer = max(loyal_customers, key=loyal_customers.get)
    best_avg_spent = loyal_customers[best_customer]

    return best_customer, best_avg_spent
	 	  	      	   	      	     	   	       	 	
