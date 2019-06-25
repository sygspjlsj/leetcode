class test:
    def process(self, gas, cost):
        left = 0
        start = 0
        total = 0
        for i in range(len(gas)):
            left += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if left < 0:
                start = i + 1
                left = 0
        if total < 0:
            return -1
        else:
            return start
