import math 
class TinyStatistician:
    def mean(arr):
        if not arr:
            return None

        return sum(arr) / len(arr)

    def median(arr):
        return TinyStatistician.quartile(arr, 50)

    def quartile(arr, percentile):
        if not arr:
            return None

        return sorted(arr)[int(len(arr) * (percentile / 100))]

    def var(arr):
        if not arr:
            return None

        mean = TinyStatistician.mean(arr)
        return sum([(x - mean) ** 2 for x in arr]) / len(arr)

    def std(arr):
        if not arr:
            return None

        return math.sqrt(TinyStatistician.var(arr))