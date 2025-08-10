# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        seen_nodes = {head: 0}
        node_index = 1
        while head.next != None:
            node = head.next
            if node not in seen_nodes:
                seen_nodes[node] = node_index
                node_index += 1
                head = node
            else:
                return node
        return None
