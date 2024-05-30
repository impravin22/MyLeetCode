class Solution:
    def reverseWords(self, s: str) -> str:

        final_str = ""
        rev_str = s.split()
        for i in range(len(rev_str) - 1, -1, -1):
            
            final_str += rev_str[i]
            if i != 0:
                final_str += " "
        
        return final_str

        
        