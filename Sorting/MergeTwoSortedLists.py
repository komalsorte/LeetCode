# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode
        merged_list = []

        while l1 and l2:
            if l1.val < l2.val:
                merged_list.append(l1.val)
                l1 = l1.next
            elif l2.val > l1.val:
                merged_list.append(l2.val)
                l2 = l2.next
            else:
                merged_list.append(l1.val)
                merged_list.append(l2.val)
                l1 = l1.next
                l2 = l2.next
        print (merged_list)
    
if __name__ == '__main__':
    Solution().mergeTwoLists([1,2,4], [1,3,4])
