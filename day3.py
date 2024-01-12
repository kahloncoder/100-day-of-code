class Solution(object):
    def mergeTwoLists(self, list1, list2):
        ex=ListNode(0)
        list3= ex
        
        while list1 and list2:
            if list1.val < list2.val:
                list3.next=list1
                list1=list1.next
            else:
                list3.next=list2
                list2=list2.next
            list3=list3.next   

        list3.next=list1 or list2     

        return ex.next          
