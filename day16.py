def deleteMiddle(self, head):
        dummy = ListNode(0,head)
        slow = dummy
        fast = dummy

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next

        return dummy.next    
        
