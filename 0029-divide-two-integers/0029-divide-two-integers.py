class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dividend_abs, divisor_abs = abs(dividend), abs(divisor)
        def exponentialDivide(dividend_abs, divisor_abs):
            if divisor_abs>dividend_abs:
                return 0
            temp = divisor_abs
            factor = 1
            while divisor_abs <= dividend_abs:
                divisor_abs+=divisor_abs
                factor*=2
            factor = factor//2
            dividend_abs = dividend_abs - divisor_abs//2
            return factor + exponentialDivide(dividend_abs,temp)
        factor  = exponentialDivide(dividend_abs, divisor_abs)
        if factor>2**31 - 1 and dividend*divisor > 0:
            return 2**31 - 1
        elif factor>2**31 - 1 and dividend*divisor < 0:
            return -2**31
        return factor if dividend*divisor > 0 else -factor



        