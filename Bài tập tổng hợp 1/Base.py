
def isPerfectNumber(number : int):
    """
    Số hoàn hảo là một số nguyên dương mà tổng các ước nguyên dương thực sự của nó 
    (các ước nguyên dương ngoại trừ chính số đó) bằng chính nó. Hoàn thiện hàm isPerfectNumber(number) 
    nhận vào số nguyên dương number và trả về True nếu number là số hoàn hảo 
    và False nếu number không phải là số hoàn hảo.
    
    Ví dụ:
    input: 6
    ouput: True
    
    input: 14
    output: False
    """
    if number < 2:
        return False
        
    sum_n = sum(i for i in range(1, number) if number % i == 0)
    return number == sum_n
    
def drawPatterm(height: int):
    """
    Hãy vẽ hình vuông có chiều cao height.
    Ví dụ 
    input: 4
    output:
    ****
    *  *
    *  *
    ****
    """
    if height < 2:
        print("*" * height)
        return
    
    print("*" * height)
    for _ in range(height - 2):
        print("*"  + " " * (height -2) + "*")
    print("*" * height)

def caculateExp(x : float, n : int):
    """
    Hoàn thiện hàm tính e^x theo công thức đã cho của đề bài.
    Ví dụ:
    input: 2 100 (Tương ứng x = 2 và n = 100)
    output: 7.3890561
    """
    result = 0.0
    term = 1.0
    for i in range(n):
        result += term 
        term *= x/(i+1)
        
    return round(result, 8)
    return 0.0
    
    
    
    
    
    
    
    
    
    	 	  	      	   	      	     	   	       	 	
