class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        senders_map = [(len(message.split()), index) for index, message in enumerate(messages)]
        senders_word_cnt = {name: 0 for name in senders}
        
        for word_cnt, index in senders_map:
            senders_word_cnt[senders[index]] += word_cnt
        dict_items = list(senders_word_cnt.items())
        dict_items.sort(key = lambda value : value[1], reverse = True)
        
        max_cnt = dict_items[0][1]
        collected = []
        for i,item in enumerate(dict_items):
            if item[1] == max_cnt:
                collected.append(item)
            else:
                break
        collected.sort(reverse = True)
        return collected[0][0]