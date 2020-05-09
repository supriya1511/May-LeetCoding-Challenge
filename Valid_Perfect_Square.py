'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
'''

import math
class Solution:
    def isPerfectSquare(self, n: int) -> bool:
        i = 1
        the_sum = 0
        while the_sum < n: 
            the_sum += i 
            if the_sum == n: 
                return True
            i += 2
        return False
