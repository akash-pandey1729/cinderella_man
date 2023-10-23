class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        def getSplitLimit(split_limit):
            _sum = 0
            for i in range(1,split_limit+1):
                _sum+= (limit-3-len(str(i)) - len(str(split_limit)))
            return _sum>=len(message)

        parts_limit = 9
        if not getSplitLimit(parts_limit):
            parts_limit = 99
        if not getSplitLimit(parts_limit):
            parts_limit = 999
        if not getSplitLimit(parts_limit):
            parts_limit = 9999
        if not getSplitLimit(parts_limit):
            return []
        
        res = []
        m_index = 0
        for i in range(1, parts_limit+1):
            if m_index >= len(message): break
            length = limit - 3- len(str(i)) -len(str(parts_limit))
            res.append(message[m_index:m_index+length])
            m_index+=length
        return [f'{part}<{i + 1}/{len(res)}>' for i, part in enumerate(res)]
        
        





        