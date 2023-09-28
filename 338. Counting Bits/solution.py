#Approach 1
class Solution:
    def countBits(self, n: int) -> List[int]:
      final_list = ''
      for each in range(n+1)
        output = ''
        while each >0:
          remainder = each%2
          output = str(remainder) + output
          each = each //2
        final_list.append(output.count('1')
        return final_list
