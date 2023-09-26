#Approach 1
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int):
        max_candy = max(candies)
        results = []
        for i in range(len(candies)):
            number = candies[i] + extraCandies #approach with unoptimized time complexity.
            if number>=max_candy:
                results.append(True)
            else:
                results.append(False)

        return results

#Approach 2:
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int):
        max_candy = max(candies)
        results = []
        for i in range(len(candies)):

            if candies[i] + extraCandies>=max_candy: #approach with optimized time complexity.
                results.append(True)
            else:
                results.append(False)

        return results
