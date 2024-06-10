class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = set("aeiou")
        final_count = 0
        for i in range(len(s) - k + 1):
            count = 0
            for vowel in vowels:
                count += s[i:i+k].count(vowel)
            if final_count < count:
                final_count = count
                    

        
        return final_count


