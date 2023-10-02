class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_length, t_length = len(s), len(t)

        def rec_substr(left_index,right_index):
            if left_index == s_length:
                return True
            if right_index == t_length:
                return False
            if s[left_index]==t[right_index]:
                left_index += 1
            right_index +=1

            return rec_substr(left_index,right_index)

        return rec_substr(0,0)
