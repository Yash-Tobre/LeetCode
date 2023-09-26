#Approach
1. First we figure out the kid who has maximum candies.
2. Then we create an list where we would append our results using .append method by checking if the condition is satisfied or not.
3. Then we start a for loop with range of length of candies, it will have a time complexity of O(N).
4. Then we may a temporary variable number (to reduce the time complexity this variable can be completely avoided), which would check if we were to give all the extra candies to the ith kid, will the ith kid will have more candies than the kid with maximum number of candies.
5. If they will we append true, if they do not will append false to the list.
6. This way we get a output list with true and false values appended.

**Time Complexity**:
The function max would have a maximum time complexity of N, since it wouldd at most do N-1 comparisions.
The for loop will have a time complexity of O(N).
Hence the overall time complexity would be O(N)

**Space Complexity**:
Since there is only one variable named max_candies and which would have a constant value not matter the size of input, the space complexity is O(1). 
