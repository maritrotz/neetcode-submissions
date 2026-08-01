# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 

    def mergeTwo(self,l1,l2):
        temp = ListNode()
        node = temp
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            
            node = node.next

        if l1:
            node.next = l1

        if l2:
            node.next = l2

        return temp.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_lists = []
            for i in range(0,len(lists),2):
                list1 = lists[i]
                list2 = lists[i+1] if (i+1) < len(lists) else None
                merged_lists.append(self.mergeTwo(list1,list2))
            lists = merged_lists

        return lists[0]


        