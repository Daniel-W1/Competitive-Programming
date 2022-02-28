class Solution:
    def compress(self, chars: List[str]) -> int:
        l, h = 0, 0
        chars_copy = chars[:]
        char_index = 0
        while h < len(chars_copy):
            cur = chars_copy[l]
            while  h < len(chars_copy) and chars_copy[h] == cur:
                h += 1
            chars[char_index] = chars_copy[l]
            char_index += 1
            leng = h - l 
            if 1 < leng < 10:
                chars[char_index] = str(leng)
                char_index += 1
            elif leng >= 10:
                leng = list(str(leng))
                for n in leng:
                    chars[char_index] = n
                    char_index += 1
            l = h
            
        return char_index
                