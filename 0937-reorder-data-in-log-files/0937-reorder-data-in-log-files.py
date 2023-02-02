class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        letter_logs = []
        digit_logs = []
        
        for log in logs:
            if not log.split()[1][0].isdigit():
                letter_logs.append(log)
            else:
                digit_logs.append(log)
        
        letter_logs.sort(key = lambda value: (value.split()[1:], value[0]))
        
        return letter_logs + digit_logs