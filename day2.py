 def isPalindrome(self, x):
        t = str(x)
        reverse=t[::-1]
        if t == reverse:
            return True
        else:
            return False  
