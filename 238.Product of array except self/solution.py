'''
Approach 1, Time Complexity O(N) and Space Complexity O(N):
Step 1:  Create 3 lists with placeholder elements of the same length as original
Step 2:  Initialize a left_product variable as 1
Step 3:  Iterate through a for loop, where we calculate the product and add it to the prefix list. This product basically starts from one for the first element,
         then for the second element it is added as the product of 1 with previous element so basicaly by the end of the for loop we have a list with multiplication of all the previous 
         elements.
Step 4:  By similair logic we intialize the right_product variable as 1 and now we iterate through a for loop but in a reverse order.
Step 5:  Multiply both the lists to return an output list.
'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Declaring the lists to be used
        prefix_list = [1]* len(nums)
        suffix_list = [1] * len(nums)
        output = [1]*len(nums)

        #Starting the prefix product loop
        left_product = 1
        for i in range (0,len(nums)):
            prefix_list[i] = left_product
            left_product *= nums[i]

        #Starting the suffix product loop
        right_product = 1
        for i in range (len(nums)-1,-1,-1):
            suffix_list[i] = right_product
            right_product *= nums[i]

        #creating the output list
        for i in range(0,len(nums)):
            output[i] = prefix_list[i]*suffix_list[i]

        return output

