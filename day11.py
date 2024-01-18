        i,j=0,len(s)-1
        while i<= j and s[i]==' ':
            i += 1
        while j >= i and s[j] == ' ':
            j -= 1
        s = s[i:j+1]

        w= s.split()
        o=[]

        for k in range(len(w)-1,0,-1):
            o.append(w[k])

        o.append(w[0])

        return ' '.join(o)    
