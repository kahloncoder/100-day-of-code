 def pairSum(self, head: Optional[ListNode]) -> int:

        val=[]
        while head:
            val.append(head.val)
            head = head.next

        n =int(len(val)/2)

        max = 0

        for i in range(n):
            v = val[i] + val[len(val)-1-i]
            if v > max:
                max = v
        return max        
                
