class Solution:
    def reverseWords(self, s: str) -> str:
   
       each_word  = s.split()
       reversed_ = reversed(each_word)
       output =  ' '.join(reversed_)

       return output
        
