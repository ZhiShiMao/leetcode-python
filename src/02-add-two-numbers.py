from ListNode import ListNode


class Solution:
    """
    示例 1：
    输入：l1 = [2,4,3], l2 = [5,6,4]
    输出：[7,0,8]
    解释：342 + 465 = 807.
    示例 2：
    输入：l1 = [0], l2 = [0]
    输出：[0]
    示例 3：
    输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    输出：[8,9,9,9,0,0,0,1]
    """

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        last = 0
        head = node = ListNode()

        while l1 or l2:
            val, last = last, 0

            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next

            if val >= 10:
                last, val = 1, val - 10

            node.next = ListNode(val)
            node = node.next
        if last == 1:
            node.next = ListNode(1)
        return head.next


# if __name__ == "__main__":
#     solution = Solution()

#     test_cases = [
#         {
#             "params": {"l1": [2, 4, 3], "l2": [5, 6, 4]},
#             "results": [7, 0, 8],
#         },
#         {
#             "params": {"l1": [0], "l2": [0]},
#             "results": [0],
#         },
#         {
#             "params": {"l1": [9, 9, 9, 9, 9, 9, 9], "l2": [9, 9, 9, 9]},
#             "results": [8, 9, 9, 9, 0, 0, 0, 1],
#         },
#     ]

#     for test_case in test_cases:
#         l1 = ListNode.from_list(test_case["params"]["l1"])
#         l2 = ListNode.from_list(test_case["params"]["l2"])
#         results = solution.addTwoNumbers(l1, l2)
#         except_results = test_case["results"]
#         print(results.to_list(), except_results)
