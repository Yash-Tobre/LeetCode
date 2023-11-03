class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_num = float('inf')
        second_num = float('inf')

        for each in nums:
            if each<= first_num:
                first_num = each
            elif each <= second_num:
                second_num = each
            else:
                return True
        return False


'''
Here the algorithm is as follows:
1. Set two variables to infinity.
2. For each entry in nums list, check if the element is smaller than the first num. If it is then update the first number to that element.
3. If that condition is not satisfied, then check if it is smaller than the second smallest number, if it is then update the second number to that element.
4. Else return true.
'''

'''
Here is the example of how the logic works:
Suppose I have a list [1,2,0,3]
now a is my first number and b is my second number.
it will compare the first entry and naturally a will get updated to 1; current values of a=1, b = inf.
then for the second entry it will go into the second condition, and b will get updated; thus current values will be a=1, b=2
then for the third element it is zero, and thus a will get updated to zero. Hence we get a=0, b =2
and then the algorithm returns true when it compares the 3rd element.

Now the questions that baffled me as when the algorithm returns true a=0 with index 2, b= 2 with index 1 so how is it an increasing triplet?

Well the answer is,
if we look at the questions it becomes 
we have 4 elements, and if we sort them it becomes
0 1 2 3
so if we our a that is the first number is the smallest and b is the second smallest, and there are numbers between the minimum and our second number, it will also cover the other triplets.
Meaning counting 0,2,3 indirectly covers the sequence 1,2,3. 
The approach to this questions was tricky for me to understand.
The crux here could be to understand the interesting genralization of problem.
'''
