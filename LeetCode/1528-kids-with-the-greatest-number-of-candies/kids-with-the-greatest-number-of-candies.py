"""
Problem description:
Input parameter:
    n : number of kids
    candies -> List of intergers, each key represent a kid and value defines how many candies doe they have 
    extraCandies -> extra candies 

Expectation:
    result -> bool_array[n]:
        key -> represents the ith kid
        value -> represent `if given all the extra candies does this kid has the highest number of candies`

Note: multiple kids can have the greatest number of candies leading to multiple True in the array.
"""


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        current_greatest = max(candies)
        bool_arr = []
        for i in range(len(candies)):
            bool_arr.append(True if (candies[i] + extraCandies) >= current_greatest else False)

        return bool_arr


        