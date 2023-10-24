class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        final_int = 0
        for each in range(0,len(digits)):
            if each != len(digits)-1:
                final_int = final_int + digits[each] * 10**(len(digits)-1-each)
            else:
                final_int += digits[-1]+1
        output = []
        for each in str(final_int):
            output.append(int(each))
        return output




