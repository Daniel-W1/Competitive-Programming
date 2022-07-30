class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        joined = ""
        cnt = Counter(words2[0])
        for i in range(1, len(words2)):
            cnt2 = Counter(words2[i])
            for char in cnt2:
                if char not in cnt:
                    cnt[char] = cnt2[char]
                else:
                    cnt[char] = max(cnt[char], cnt2[char])
        output = []
        for word in words1:
            count = Counter(word)
            check = True
            for char in cnt:
                if char not in count or cnt[char] > count[char]:
                    check = False
                    break
            if check:
                output.append(word)
        return output