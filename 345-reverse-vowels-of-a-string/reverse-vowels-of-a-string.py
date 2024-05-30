class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        str_split = [i for i in s]
        final_str = ""
        str_index = []
        vowel_ls = []
        for i in range(len(str_split)):
            if str_split[i] in vowels:
                vowel_ls.append(str_split[i])
                str_index.append(i)
        vowel_ls.reverse()
        for i in range(len(str_index)):
            str_split[str_index[i]] = vowel_ls[i]
        
        for i in str_split:
            final_str += i
        
        return final_str
        