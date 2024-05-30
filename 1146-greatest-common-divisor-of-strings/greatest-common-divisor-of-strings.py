class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        a = len(str1)
        b = len(str2)
        
        if str1 == str2:
            return str1
        
        if a > b:
            str1, str2 = str2, str1
        
        for i in range(len(str1), 0, -1):
            substr = str2[:i]
            if str1 == substr * (len(str1) // len(substr)) and str2 == substr * (len(str2) // len(substr)):
             return substr
        
        return ""    