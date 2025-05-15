class ComplexNumber:
    '''
    Lớp thực hiện tạo đối tượng số phức cùng với các phép toán cơ bản,
    số phức (a + bi) có phần thực và phần ảo là số thực
    '''
    
    def __init__(self, real, image):
        '''
        Hàm dựng  của số phức  gồm phần thực real và phần ảo image
        '''
        self.real = real
        self.image = image
    
    def addComplex(self, com):
        '''
        Phép cộng số phức
        '''
        return ComplexNumber(self.real + com.real, self.image + com.image)
    
    def subComplex(self, com):
        '''
        Phép trừ số phức
        '''
        return ComplexNumber(self.real - com.real, self.image - com.image)
        
    def multiComplex(self, com):
        '''
        Phép nhân số phức:
        (a + bi)(c + di) = (ac - bd) + (ad + bc)i
        '''
        a, b = self.real, self.image
        c, d = com.real, com.image
        real_part = a * c - b * d
        image_part = a * d + b * c
        return ComplexNumber(real_part, image_part)
    
    def divComplex(self, com):
        '''
        Phép chia số phức:
        (a + bi)/(c + di) = [(ac + bd) + (bc - ad)i] / (c^2 + d^2)
        '''
        a, b = self.real, self.image
        c, d = com.real, com.image
        denominator = c ** 2 + d ** 2
        real_part = (a * c + b * d) / denominator
        image_part = (b * c - a * d) / denominator
        return ComplexNumber(real_part, image_part)
    
    def toString(self):
        '''
        Hàm trả lại chuỗi biểu diễn số phức với phần thực và phần ảo làm tròn đến 3 chữ số
        '''
        return str(round(self.real, 3)) + ' + ' + str(round(self.image, 3)) + 'i'


def testDemo():
   
    a = ComplexNumber(2, 3)
    b = ComplexNumber(4, 5)
    
    print(a.addComplex(b).toString())
    print(a.subComplex(b).toString())
    print(a.multiComplex(b).toString())
    print(a.divComplex(b).toString())

'''
Bỏ comment lệnh testDemo() dưới đây để chạy test chương trình, và comment lại lệnh đó khi nộp bài
'''
#testDemo()

	 	  	      	   	      	     	   	       	 	
