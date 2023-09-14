class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        emp = ""
        if len(word1)> len(word2):
            a = word1[0:len(word2)]
            for i in range(len(word2)):
                emp = emp+a[i]
                emp = emp+word2[i]
            emp = emp + word1[len(word2):]

        elif len(word2)> len(word1):
            a = word2[0:len(word1)]
            for i in range(len(word1)):
                emp = emp+word1[i]
                emp = emp+a[i]
            emp = emp + word2[len(word1):]
        
        else:
            for i in range(len(word1)):
                emp = emp+word1[i]
                emp = emp+word2[i]
         
        
        return emp

        
