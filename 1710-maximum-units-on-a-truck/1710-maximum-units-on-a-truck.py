class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        freq, max_units = [0]*1001, 0
        for box in boxTypes:
            freq[box[1]] += box[0]
        
        for units in range(1000,0,-1):
            if truckSize < 0: break
            max_units += min(truckSize, freq[units]) * units
            truckSize -= freq[units]
        return max_units