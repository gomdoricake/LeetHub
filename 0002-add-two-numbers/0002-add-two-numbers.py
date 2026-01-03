# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr_first = ptr_result = ListNode()

        flag = 0
        first = True
        while True: 
            add = int(l1.val) + int(l2.val) + flag
            if first: 
                ptr = ListNode(add)
                first = False

            if add > 9: 
                flag = 1
                ptr = ListNode(add - 10)
            else: 
                flag = 0
                ptr = ListNode(add)

            ptr_result.next = ptr  
            ptr_result = ptr  
            l1 = l1.next
            l2 = l2.next

            if l1 == None and l2 == None and flag == 1: 
                ptr = ListNode(1)
                ptr_result.next = ptr

            if l1 == None or l2 == None: 
                break


        # ptr_l2 가 끝났을 때.
        while l1 != None:
            add = int(l1.val) + flag

            if (add > 9):         
                flag = 1  
                ptr = ListNode(add - 10) 
            else: 
                flag = 0     
                ptr = ListNode(add)        

            ptr_result.next = ptr
            ptr_result = ptr       
            l1 = l1.next     

            if l1 == None and flag == 1: 
                ptr = ListNode(1)
                ptr_result.next = ptr


        while l2 != None: 
            add = int(l2.val) + flag

            if (add > 9): 
                flag = 1
                ptr = ListNode(add - 10)
            else: 
                flag = 0
                ptr = ListNode(add)

            ptr_result.next = ptr
            ptr_result = ptr
            l2 = l2.next     

            if l2 == None and flag == 1: 
                ptr = ListNode(1)
                ptr_result.next = ptr

        return ptr_first.next
