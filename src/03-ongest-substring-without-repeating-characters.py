class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slide, ret = [], 0
        for i in range(len(s)):
            if s[i] in slide:
                index = slide.index(s[i])
                ret = max(ret, len(slide))
                slide = slide[index+1:]
            slide.append(s[i])
        return max(ret, len(slide))

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slide, ret = [], 0
        for i in range(len(s)):
            index = -1
            for j in range(len(slide)):
                if s[i] == slide[j]:
                    index = j
                    break
            if index >= 0:
                ret = max(ret, len(slide))
                slide = slide[index + 1 :]
            slide.append(s[i])
        return max(ret, len(slide))


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        {
            "params": {"s": "abcabcbb"},
            "results": 3,
        },
        {
            "params": {"s": "bbbbb"},
            "results": 1,
        },
        {
            "params": {"s": "pwwkew"},
            "results": 3,
        },
        {
            "params": {"s": ""},
            "results": 0,
        },
        {
            "params": {"s": "ojyseenuxxpohrysqixldpki"},
            "results": 12,
        },
        {
            "params": {"s": " "},
            "results": 1,
        }
    ]

    for test_case in test_cases:
        results = solution.lengthOfLongestSubstring(**test_case["params"])
        except_results = test_case["results"]
        print(results, except_results)