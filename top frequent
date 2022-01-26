def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count= Counter(nums)
        collector= []

        for ke, v in count.items():
            collector.append((ke,v))
        collector = sorted(collector, key= lambda val: val[1], reverse = True)

        ans=[]

        if k ==1:
            return [collector[0][0]]

        for i in range(k):
            ans.append(collector[i][0])

        return ans
