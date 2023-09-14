The Goal
We have two words, we have to take single letter from each string (starting from the first word) and arrange them alternatively.

The Approach
1. Compare both words and determine the one longer in length
2. Slice the longer string into the size equal to the smaller one
3. Start adding letters to an empty string, from equal sized string, beginning with the first word. Let us call that new string
4. Add the remaining part of the longer string ( The one we cut off during slicing in step 2) to the new string.
5. Return the resuly.

Let me know what you think.
