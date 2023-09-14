class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=''
        sorted_string = sorted(strs)
        first = sorted_string[0]
        last = sorted_string[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans


        

        
        
