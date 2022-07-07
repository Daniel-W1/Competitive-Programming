class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        senders_map = [(len(message.split()), index) for index, message in enumerate(messages)]
        senders_word_cnt = {name: 0 for name in senders}
        
        for word_cnt, index in senders_map:
            senders_word_cnt[senders[index]] += word_cnt
        dict_items = list(senders_word_cnt.items())
        max_cnt = max(senders_word_cnt.values())
        
        max_name = None
        for key, value in senders_word_cnt.items():
            if senders_word_cnt[key] == max_cnt:
                if not max_name:
                    max_name = key
                else:
                    max_name = max(max_name, key)
        return max_name