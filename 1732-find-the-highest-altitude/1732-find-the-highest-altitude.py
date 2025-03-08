class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        r=0
        arr=[]
        arr.append(r)
        for i in gain:
            
            r= r+i
            arr.append(r)
        print(arr)
        return max(arr)