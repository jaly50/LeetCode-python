class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        carry =1
        for i in range(len(digits)-1, -1, -1):
            carry = digits[i]+carry
            carry, digits[i] = divmod(carry, 10)
            # or
            #digits[i] = carry % 10
            #carry = carry / 10
        if carry:
            digits.insert(0, carry)
        return digits
        
