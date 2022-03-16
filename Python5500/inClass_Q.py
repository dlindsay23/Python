import numpy as np


f = open("/home/ubuntu/environment/data5500_sp22/week6_queues_stacks/zoomsession2/KO.txt", "r")
# lines = f.readlines()
# print("lines: ", lines)

prices = []
line = f.readline()

buy = 0
tot_profit = 0
while line:
    prices.append(float(line))
    line = f.readline()

    if len(prices) == 6: # 5 day moving average + 1 current day price
        avg = np.mean(prices[0:5])
        # print("avg: ", avg)
        if prices[5] < avg * 0.98 and buy == 0:
            buy = prices[5]
        elif prices[5] < avg * 1.02 and buy != 0:
            tot_profit += prices[5] - buy
            buy = 0
        else:
            pass #do nothing
        prices.pop(0)
        
print("tot_profit: ", tot_profit)
print("percenage return: ", tot_profit/prices[0])
