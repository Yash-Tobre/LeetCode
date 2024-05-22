class Solution:
    
    def decodeString(self, s: str) -> str:

        stack = []
        num = 0
        current_string = ""

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '[':
                stack.append((num, current_string))
                num=0
                current_string = ""
            elif char == ']':
                last_num, last_str = stack.pop()
                current_string = last_str + (current_string*last_num)
            else:
                current_string += char
        
        return current_string
       
