class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int):
        max_candy = max(candies)
        results = []
        for i in range(len(candies)):
            number = candies[i] + extraCandies
            if number>=max_candy:
                results.append(True)
            else:
                results.append(False)

        return results
