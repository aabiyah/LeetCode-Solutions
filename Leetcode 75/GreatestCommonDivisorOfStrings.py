# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"class 

Solution(object):
    def gcdOfStrings(self, str1, str2):
        def gcd(a, b):
            while b != 0:         # Continue until the remainder is zero
              a, b = b, a % b     # Assign b to a and the remainder of a divided by b to b
            return a              # When b is zero, a is the GCD

        # An implementation of the Euclidean algorithm for finding the greatest common divisor (GCD) of two integers a and b.

        if str1 + str2 != str2 + str1:
            return ""

        gcd_length = gcd(len(str1), len(str2))
        return str1[:gcd_length]