class Solution:
    def romanToInt(self, s: str) -> int:
        Rom_Dict = {'I':1 ,'V':5 , 'X':10 , 'L':50 , 'C':100 , 'D':500 , 'M':1000}
        N = 0
        for i in range(len(s)-1):
            if (Rom_Dict[s[i]] < Rom_Dict[s[i+1]]):
                N-=Rom_Dict[s[i]]
            else:
                N+=Rom_Dict[s[i]]
                
        return N+Rom_Dict[s[-1]]