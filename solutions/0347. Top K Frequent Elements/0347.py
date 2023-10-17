# Time complexity : O(n)
# Space complexity: O(n)

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num,0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]        
        for num, count in counts.items():
            buckets[count].append(num)
        
        topK = []
        for i in range(len(buckets)-1, -1, -1):
            for element in buckets[i]:
                topK.append(element)
                k -= 1
                if k == 0:
                    return topK

# Time complexity : O(nlogn)
# Space complexity: O(n)
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num,0) + 1
        
        (num, count)        
        items = list(counts.items())
        items.sort(key=lambda x: x[1], reverse=True)        
        
        topK = [item[0] for item in items[:k]]
        return topK
        