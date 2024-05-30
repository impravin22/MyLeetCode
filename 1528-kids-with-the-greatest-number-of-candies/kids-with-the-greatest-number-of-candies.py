class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        # bool_list = []
        max_candies = max(candies)
        # for candy in candies:
        #     bool_list.append((candy + extraCandies) >= max_candies)
        
        return [((candy + extraCandies) >= max_candies) for candy in candies]
        