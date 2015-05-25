class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    # scarlett Chen
    # 5/25/22015 Mon 4:02 pm - 4.31 pm 
    # 43	Multiply Strings
    # though: reverse string, traverse num1: traverse num2: f[n1+n2-1] = (num1[n1] * num2[n2] + carry)/10
    def multiply(self, num1, num2):
        result = 0
        for i,digit1 in enumerate(num1[::-1]):
            x1 = int(digit1)*(10**i)
            for j, digit2 in enumerate(num2[::-1]):
                x2 = int(digit2) * (10**j)
                result += x1*x2
        return str(result)
