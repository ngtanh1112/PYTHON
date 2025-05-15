

def find_minimum_sum(nums):
    """
    Tìm đỉnh núi có tổng nhỏ nhất.
    Cho một danh sách số nguyên dương nums
    Bộ 3 chỉ số i, j, k được gọi là đỉnh núi nếu thỏa mãn:
    i < j < k và nums[i] < nums[j] và nums[j] > nums[k]
    Ví dụ 1: input [8,6,1,5,3]
    với i = 2, j = 3 k = 4 tương ứng tạo thành một đỉnh núi với tổng bằng 9 (1 + 5 + 3)
    output: 9
    Ví dụ 2: input [5,4,8,7,10,2]
    i = 0, j = 2, k = 5 tạo thành một đỉnh núi với tổng bằng 15.
    i = 1, j = 4, k = 5 tạo thành một đỉnh núi với tổng bằng 16.
    output : 13
    Nếu không tồn tại đỉnh núi nào trong danh sách
    output : -1
    """
    n = len(nums)
    min_sum = float('inf')
    found = False

    for j in range(1, n-1):
        left_min = float('inf')
        # Tìm i < j sao cho nums[i] < nums[j] nhỏ nhất
        for i in range(j):
            if nums[i] < nums[j]:
                if nums[i] < left_min:
                    left_min = nums[i]

        right_min = float('inf')
        # Tìm k > j sao cho nums[k] < nums[j] nhỏ nhất
        for k in range(j+1, n):
            if nums[k] < nums[j]:
                if nums[k] < right_min:
                    right_min = nums[k]

        if left_min != float('inf') and right_min != float('inf'):
            found = True
            s = left_min + nums[j] + right_min
            if s < min_sum:
                min_sum = s

    if found:
        return min_sum
    else:
        return -1

import math

def tich2Vec(v1, v2):
    tich = 0
    for i in range (len(v1)):
        tich = tich + v1[i]*v2[i]
    return tich
    
def doDai(v):
    result = 0
    for i in range (len(v)):
        result = result + v[i]**2
    return math.sqrt(result)
def cosin_distance(v1, v2):
    """
    Tính khoảng cách cosin của 2 vector,
    input: v1, v2 là danh sách có cùng kích thước
    Cosin distance được tính theo công thức:
    cho trong đề bài.
    """

    
    return tich2Vec(v1,v2)/(doDai(v1)*doDai(v2))


    
def get_hightest_gdp(country_list):
    """
    country_list là một danh sách trong đó mỗi phần tử là một tuple có cấu trúc như sau:
    (country_id, region, gdp, area)
    country_id: mã quốc gia
    region: khu vực (Asia, EU, USA...)
    gdp: tổng thu nhập quốc dân
    area: diện tích tương ứng với quốc gia đó
    tìm ra và trả về một danh sách 3 mã quốc gia
    có chỉ số gdp cao nhất được sắp xếp giảm dần theo chỉ số gdp, nếu cùng chỉ số gdp thì sắp giảm dần theo mã quốc gia country_id
    """
    
    sorted_list = sorted(country_list, key=lambda x: (x[2], x[0]), reverse=True)
    top3 = sorted_list[:3]
    # Lấy danh sách country_id
    return [item[0] for item in top3]	 	  	      	   	      	     	   	       	 	
