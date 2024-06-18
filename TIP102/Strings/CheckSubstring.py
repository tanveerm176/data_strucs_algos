# https://guides.codepath.org/compsci/Substring#2-m-atch


class Solution:
    def substring(self, large_str: str, potential_substr: str) -> bool:
        substr_len = len(potential_substr)
        large_str_len = len(large_str)

        for i in range(large_str_len - substr_len+1):
            for j in range(substr_len):
                


solution = Solution()

solution.substring("laboratory", "rat")
