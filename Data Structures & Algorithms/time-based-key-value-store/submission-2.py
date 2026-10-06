class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d:
            self.d[key][timestamp] = value
        else:
            self.d[key] = {timestamp: value}

    def get(self, key: str, timestamp: int) -> str:
        if key in self.d:
            if timestamp in self.d[key]:
                return self.d[key][timestamp]
            elif timestamp > max(self.d[key].keys()):
                return self.d[key][max(self.d[key].keys())]
            elif timestamp < max(self.d[key].keys()) and timestamp > min(self.d[key].keys()):
                #search for the bigest timestamp smaller than t
                ind = biggest_val_smaller_than_t(list(self.d[key].keys()), timestamp)
                val = self.d[key][ind]
                return val
            else:
                return ""
        else:
            return ""

def biggest_val_smaller_than_t(l: List, t: int) -> int:
    start, end = 0, len(l) - 1 
    l = sorted(l)
    biggest = start
    while start <= end:
        mid = (start + end) // 2
        if l[mid] > t:
            end = mid - 1 
        else:
            if l[mid] > biggest:
                biggest = l[mid]
            start = mid + 1
    return biggest
            


