Step 1: We define a prefix as the first string of the list.
Step 2: We iterate through the remaining words of the list.
Step 3: We have a variable 'i', to make sure it is smaller than the first string, we put the condition i<len(prefix)
Step 4: i should also be smaller than the word we are comparing it with.
Step 5: Then we check if the first letter of i, is equal to the first letter of the word.
Step 6: If the condition is satisfied, we increase the counter of i.
Step 7: Then we extract, the sliced version up untill i.

Example:
['Drowning','Drone','Drapion']
Now let our prefix be:
Prefix = 'Drowning'
Then 
iteration 1:
word = Drone
the value of i is zero currently.
we check our if conditions.
1. i < len(drowning) satsisfied.
2. i < len(drone) satisfied.
3. first word of drowning is equal to first word of drone.
4. i = 1 now.

Similiarly in the second iteration,
value of i is one,
and all the three conditions are satisfied.
so value of i goes to 2.

In the third iteration,
value of i is 2,
all the conditions are satisfied,
value of i goes to 3.

In the 4th iteration,
the third condition is not satisfied,
so we exit the while loop 

Now currently prefix is 'dro'.

we go to the next word which is drapion.
and now, it will only extract the common words from the prefix following the similiar steps. Thus our prefix become 'dr'.

Hence now we have our final answer.

Time Complexity: O(m*n) where m is the length of the longest word since we may have to go through each word, and N is the number of words in the list.
Space Complexity: O(1) since we have data structures that take a constant amount of memory, throughout that does not change with input.
