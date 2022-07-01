class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda box:box[1],reverse = True)
        units = 0
        for size,unit in boxTypes:
            if truckSize > size:
                truckSize -= size
                units += size*unit
            elif truckSize > 0:
                units += truckSize*unit
                break
        return units
            
            