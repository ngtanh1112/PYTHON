import math

class Fraction:
    '''
     Lớp thực hiện tạo đối tượng phân số cùng với các phép toán phân số
    '''

    def __init__(self, numerator, denominator):
        '''
        Khởi tạo tử số và mẫu số
        '''
        self.numerator = numerator
        self.denominator = denominator
        self.simplifySelf()

    def simplifySelf(self):
        '''
        Tối giản chính đối tượng phân số hiện tại
        '''
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

        # Nếu mẫu âm, chuyển dấu lên tử
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def simplify(self, frac):
        '''
        Tối giản phân số khác (không phải chính nó)
        '''
        gcd = math.gcd(frac.numerator, frac.denominator)
        num = frac.numerator // gcd
        den = frac.denominator // gcd

        # Nếu mẫu âm, chuyển dấu lên tử
        if den < 0:
            num *= -1
            den *= -1

        return Fraction(num, den)

    def addFraction(self, frac):
        num = self.numerator * frac.denominator + frac.numerator * self.denominator
        den = self.denominator * frac.denominator
        return self.simplify(Fraction(num, den))

    def subFraction(self, frac):
        num = self.numerator * frac.denominator - frac.numerator * self.denominator
        den = self.denominator * frac.denominator
        return self.simplify(Fraction(num, den))

    def multiFraction(self, frac):
        num = self.numerator * frac.numerator
        den = self.denominator * frac.denominator
        return self.simplify(Fraction(num, den))

    def divFraction(self, frac):
        num = self.numerator * frac.denominator
        den = self.denominator * frac.numerator
        return self.simplify(Fraction(num, den))

    def toString(self):
        return str(self.numerator) + '/' + str(self.denominator)


def testDemo():

    a = Fraction(2,3)
    b = Fraction(7,3)
    
    print(a.addFraction(b).toString())
    print(a.subFraction(b).toString())
    print(a.multiFraction(b).toString())
    print(a.divFraction(b).toString())

'''
Bỏ comment lệnh testDemo() dưới đây để chạy chương trình, và comment lại lệnh đó khi nộp bài
'''
#testDemo()	 	  	      	   	      	     	   	       	 	
