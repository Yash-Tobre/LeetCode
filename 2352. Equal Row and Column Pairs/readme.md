The approach to this question is pretty simple.
Just as the human intution would work, we want to find a way to look at the numbers from the row, and then from the column and in the end compare both.
The steps are like this:
1. Iterate through the grid, and make a tuple of each of the lists we have (rows) and increment the count to 1.
2. Iterate through the grid, first through the rows and then through the tuple that we create using another for loop, thus obtaining the column tuple.
3. Check if this column tuple is already in the row dict that we created, and increment the count by 1 if it is.

In this way, we store row information, compare it with columns to increment the count.
