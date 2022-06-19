class MagicDictionary:

    def __init__(self):
        self.dict = {}        

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            res = self.dict.get(len(word),set())
            self.dict[len(word)] = res.union(set([word]))
    def search(self, searchWord: str) -> bool:
        words = self.dict.get(len(searchWord),set())
        for word in words:
            cnt = 0
            for i in range(len(word)):
                if word[i] != searchWord[i]:
                    cnt +=1 
            if cnt == 1:
                return True
        return False
