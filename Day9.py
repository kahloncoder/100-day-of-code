 def removeStars(self, s):
        stack= ""

      
        for i in s:
            if i != '*':
                stack += i
            else:
                stack = stack[:-1]

        return stack       
