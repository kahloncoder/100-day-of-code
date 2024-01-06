def mergeAlternately(self, word1: str, word2: str) -> str:
           merged=[]
           minl=min(len(word1),len(word2))                    
           for i in range(minl):               
                merged.append(word1[i])               
                merged.append(word2[i])    
           merged.extend([word1[minl:],word2[minl:]])            
           return ''.join(merged) 
