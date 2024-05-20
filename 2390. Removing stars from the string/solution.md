
class Solution:
    
    def removeStars(self, s: str) -> str:
        output_list = [] 
        for char in s:
            if char == '*':
                if output_list:
                    output_list.pop()
            else:
                output_list.append(char)
        
        return ''.join(output_list)

The above code is the python solution of the problem. 
The intution is kind of trying to take each item from the string, consider it like an bucket full of items. Then put it in another bin, and if you encounter a star from the bucket, you remove the last element inserted in the bin as well.

As of the solution, 
we first iterate through the string. If the character we encounter is star, we do not add it into our output list but instead we pop the last output given to the list. Otherwise we just add the character to the list.
