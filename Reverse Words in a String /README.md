#Approach

We use the built in Python methods to simplify this code:
1. Split method: This methods by default splits on each space, tab and indents and returns you a string list without any spaces.
2. reversed method: This methods reverses the elements in the list.
3. .join method: This method joins the elements of the list using a white space between them. That is why we use ' '.join(reversed string)

**Time Complexity**: _O(N)_
- Since the split method, in worst case can go through the whole string once, hence it has a complexity of O(N).
- Reversed method, similiarly can go through the list N times in the worst case where the list is in reverse order.
- join method, is a concatenation operation, which takes O(N) complexity in the worse case.

**Space Complexity**: _O(N)_
- Split method breaks down an input string on n words, hence it has space complexity O(N).
- reversed method returns as an iterator and thus has a constant space complexity of O(1).
- the join operation takes O(N) space complexity as it is entirely dependant on the input size.
