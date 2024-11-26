class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length_word = strs[0]
        
        for i in range(1, len(strs)):
            if len(min_length_word) > len(strs[i]):
                min_length_word = strs[i]
                print("La chaine minimal est : " + min_length_word)

        lcp = ""

        for j in range(len(min_length_word)):
            for word in strs:
                if word[j] != min_length_word[j]:
                    return (lcp)
            lcp += min_length_word[j]

        return (lcp)