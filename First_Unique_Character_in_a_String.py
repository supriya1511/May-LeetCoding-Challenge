'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        flag=1
        magazineCnt = collections.Counter(s)
        for k,v in magazineCnt.items():
            if v==1:
                flag=0
                break
        if(flag==0):
            return s.index(k)
        else:
            return -1     
