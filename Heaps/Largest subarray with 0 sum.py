def maxLen(self, n, arr):
        #Code here
        d = dict()
        sums = 0
        maxi = 0
        for i in range(n):
            sums += arr[i]
            
            if sums == 0:
                maxi = i + 1
                continue
            
            if sums not in d:
                d[sums] = i
            else:
                if i - d[sums] > maxi:
                    maxi = i - d[sums]
                    
        return maxi
