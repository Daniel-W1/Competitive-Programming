class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt_different = Counter()
        cnt_same = Counter()
        
        for word in words:
            if word[0] != word[1]:
                cnt_different[word] += 1 
            else:
                cnt_same[word] += 1
        
        answer = 0
        # now do for the different elements
        for word in cnt_different:
            answer += min(cnt_different[word], cnt_different[word[::-1]])*4
            cnt_different[word] = 0
        
        # now for the same elements
        max_odd = 0
        for word in cnt_same:
            if not cnt_same[word]%2:
                answer += (cnt_same[word]*2)
            else:
                answer += ((cnt_same[word] - 1)*2)
                max_odd = max(max_odd, cnt_same[word])
        
        if max_odd:
            answer -= (max_odd - 1) * 2
            answer += max_odd * 2
        
        return answer
        