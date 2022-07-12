class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired = [(pos, spd) for pos,spd in zip(position, speed)]
        paired.sort(reverse = True)
        stack = []
        for pos,spd in paired:
            time = (target-pos)/spd
            if not stack or stack[-1] < time:
                stack.append(time)
        return len(stack)
    