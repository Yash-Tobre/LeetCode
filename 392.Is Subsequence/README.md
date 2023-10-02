Step 1: If the each character of a string is equal to each character of a target string.  
Step 2: If it is, then we increament the index position and call the function again. Hence a recursive function.  
Step 3: In our function, we have two conditions: First one checks if the index pointer for the substring has reached the length of the string, if that is the case that means we were able to match all of the characters.  
The second condition checks if the right index matches the length of the target string. If it does, it implies that we traversed through the target string without fully traversing through the substring, and thus could not find the subsequence.Hence the first condition returns True and the second condition returns false.  
Step 4: We return this function by starting with the indexes 0 and 0 for both the pointers, and recursively call it.

**Time Complexity**  
The Time complexity is O(T) since the target string is most likley to be bigger between the both.  

**Space Complexity**  
The space complexity is also O(T) since we might have T recursions. Each recursive function call has a call stack associated with it which contains variables, return addresses and so on.
