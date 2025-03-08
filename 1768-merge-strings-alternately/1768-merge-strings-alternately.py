class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=""
        for i in range((max(len(word1),len(word2)))):
            if len(word1) > i:
                s += word1[i]
            if len(word2) > i:
                s += word2[i]
        return s

