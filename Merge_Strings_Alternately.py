class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_str=""
        if len(word1) > len(word2):
            for i in range(len(word1)):
                merged_str += word1[i]
                if i < len(word2):
                    merged_str += word2[i]
        elif len(word2) > len(word1):
            for i in range(len(word2)):
                if i < len(word1):
                    merged_str += word1[i]
                merged_str += word2[i]
        else:
            for i in range(len(word1)):
                merged_str += word1[i]
                merged_str += word2[i]
        return merged_str

        
            

