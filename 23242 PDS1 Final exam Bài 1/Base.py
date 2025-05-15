
def max_pooling(arr):
    """
    Cho một danh sách arr gồm n phần tử mỗi phần tử là một danh sách n số nguyên.
    Có thể hình dung arr như một ma trận vuông có số chiều là (n, n).
    n là một số chẵn (2,4,6,8...)
    
    Sử dụng một cửa sổ trượt có kích thước 2x2 lần lượt trượt qua ma trận arr
    xuất phát từ vị trí 0,0. Bước nhảy của cửa sổ trượt là 2.
    
    Tại mỗi vị trí trả về giá trị max của cửa sổ trượt vào ma trận kết quả đầu ra.
    
    Ví dụ: input = [[5,2,3,8],
                    [4,1,6,1],
                    [5,2,9,7],
                    [2,3,1,8]]
                    
            output = [[5,8],
                      [5,9]]
                      
            Trong ví dụ trên cửa sổ trượt (2,2) áp lần lượt vào các vị trí (0,0) (0,2),(2,0),(2,2)
    """
    n = len(arr)
    result = []
    for i in range(0, n, 2):
        row = []
        for j in range(0, n, 2):
            # Lấy cửa sổ 2x2
            window = [arr[i][j], arr[i][j+1], arr[i+1][j], arr[i+1][j+1]]
            row.append(max(window))
        result.append(row)
    return result
    
def find_anagram_index(s, x):
    """
    Chuỗi y được gọi là một anagram của chuỗi x nếu hoán vị các ký tự của y == x.
    Ví dụ: cho chuỗi x: abc thì các chuỗi sau là anagram của x: abc, acb, bac, bca, cab, cba
    
    Tìm và trả ra tất cả index của chuỗi s sao cho từ vị trí index có thể lấy được
    chuỗi con của s là anagram của x.
    
    Ví dụ s: cbaebabacd x : abc
    tại index 0 có chuỗi cba
    tại index 6 có chuỗi bac
    output: [0, 6]
    
    Ví dụ s: abab x: ab
    output: [0, 1, 2]
    
    Gợi ý: có thể sử dụng sorted() để xác định tính chất anagram của 2 chuỗi.
    Nếu không tồn tại chỉ số nào, trả về một danh sách trống.
    """
    len_x = len(x)
    sorted_x = ''.join(sorted(x))
    result = []
    for i in range(len(s) - len_x + 1):
        substr = s[i:i+len_x]
        if ''.join(sorted(substr)) == sorted_x:
            result.append(i)
    return result
    
    
def sort_common(a , b):
    """
    Cho a, b là 2 danh sách chứa các phần tử là các tuple có cấu trúc sau ('a', 1) trong đó
    phần tử đầu tiên là ký tự.
    phần tử thứ 2 là số lần xuất hiện của ký tự đó.
    Mỗi tuple trong danh sách là duy nhất không tồn tại tuple thứ hai giống với chính tuple đó.
    
    Tìm trả về một danh sách c chứa các tuple xuất hiện trong cả a và b,
    c được săp xếp tăng dần theo số lần xuất hiện, nếu số lần xuất hiện giống nhau thì 
    xắp sếp tăng dần theo thứ tự từ điển của các ký tự.
    
    Ví dụ: input:
    a: [('p', 2), ('h', 6), ('w', 6), ('l', 8), ('s', 1), ('l', 6), ('t', 5), ('n', 7), ('w', 8), ('x', 2)]
    b: [('p', 2), ('h', 6), ('w', 6), ('n', 9), ('i', 1), ('p', 6), ('b', 2), ('k', 2), ('f', 5), ('u', 8)]
    output:
    [('p', 2), ('h', 6), ('w', 6)]
    
    Gợi ý: Sử dụng tính chất của set để lấy ra các phần tử chung trong 2 danh sách.
    Nếu không tồn tại chỉ số nào, trả về một danh sách trống.
    """
    set_a = set(a)
    set_b = set(b)
    common = list(set_a & set_b)
    # Sắp xếp tăng dần theo số lần xuất hiện, nếu bằng thì theo thứ tự từ điển
    common.sort(key=lambda t: (t[1], t[0]))
    return common
    
    
def validate_mobile_number(list_mobile):
    """
    list_mobile là một danh sách trong đó mỗi phần tử là một tuple có cấu trúc sau:
    sdt : (str) thông tin về số điện thoại của khách hàng.
    adress: (str) thông tin về địa chỉ khách hàng (HN hoặc HCM)
    servicer: (str) thông tin về nhà mạng cung cấp dịch vụ (Viettel hoặc VNPT)
    
    Một số điện thoại được coi là True nếu:
    Nếu nhà mạng là Viettel thì 3 số đầu phải là một trong 3 số sau: 
    ['096', '097', '098'] 
    Nếu nhà mạng là VNPT thì 3 số đầu phải là một trong 3 số sau:
    ['089', '090', '093']
    
    Nếu adress là Hà Nội thì tổng 4 số cuối là số lẻ.
    Nếu adress là Hồ Chí Minh thì tổng 4 số cuối là số chẵn.
    output: list[bool] tương ứng với giá trị True/False mỗi tuple trong list_mobile
    
    Ví dụ: 
    (0961231235,HN,Viettel) -> True.
    (0931231234,HCM,Viettel) -> False. | sai đầu số
    (0931231234,HCM,VNPT) -> True
    (0931231235,HCM,VNPT) -> False | HCM có tổng 4 số cuối lẻ.
    
    output: [True, False , True, False]
    """
    result = []
    viettel_prefix = ['096', '097', '098']
    vnpt_prefix = ['089', '090', '093']
    for sdt, adress, servicer in list_mobile:
        prefix = sdt[:3]
        last4 = sdt[-4:]
        # Kiểm tra nhà mạng và đầu số
        if servicer == 'Viettel':
            if prefix not in viettel_prefix:
                result.append(False)
                continue
        elif servicer == 'VNPT':
            if prefix not in vnpt_prefix:
                result.append(False)
                continue
        else:
            # Nhà mạng khác, False
            result.append(False)
            continue

        # Tính tổng 4 số cuối
        sum_last4 = sum(int(ch) for ch in last4)
        if adress == 'HN':
            # Tổng 4 số cuối phải lẻ
            result.append(sum_last4 % 2 == 1)
        elif adress == 'HCM':
            # Tổng 4 số cuối phải chẵn
            result.append(sum_last4 % 2 == 0)
        else:
            # Địa chỉ khác -> False
            result.append(False)
    return result	 	  	      	   	      	     	   	       	 	
