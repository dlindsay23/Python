# import json

# # the following code is for the in class exercise for zoom session 10.1

# # As a class we will add the following:
# # 1. define a function to run the strategy, and return profit and returns
# # 2. add the results to a dictionary
# # 3. save the results to a json file

# # Steps required to finish your homework:
# # 1. mean reversion function
# # 2. saveResults function
# # 3. collect data for all tickers
# # 4. run for all tickers

# def simpleMovingAverage(prices):
#     i = 0
#     buy = 0
#     total_profit = 0
#     first_buy = 0
#     for p in prices:
#         if i >= 5: 
#             moving_average = (prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5]) / 5
            
#             #simple moving average logic, not mean
#             if p > moving_average and buy == 0: #buy
#                 print("buying at: ", p)
#                 buy = p
#                 if first_buy == 0:
#                     first_buy = p
#             elif p < moving_average and buy != 0: #sell
#                 print("selling at: ", p)
#                 print("trade profit: ", p - buy)
#                 total_profit += p - buy
#                 buy = 0
#         i += 1
        
#     final_percentage = (total_profit / first_buy) * 100
#     print("first buy: ", first_buy)
#     print("total profit: ", total_profit)
#     print("final percentage: ", final_percentage, "%")
    
#     return total_profit, final_percentage
        
# tickers = ["TSLA"]
# results = {}
# for ticker in tickers:
#     fil = open("/home/ubuntu/environment/week10/zoomsession1/" + ticker + ".txt")
#     lines = fil.readlines()
#     # print(lines)
    
#     prices = []
#     for line in lines:
#         prices.append(float(line))
        
#     total_profit, final_percentage = simpleMovingAverage(prices)
    
#     results[ticker + "_sma_profit"] = total_profit
#     results[ticker + "_sma_returns"] = final_percentage
    

# json.dump(results, open("/home/ubuntu/environment/week10/zoomsession1/results.json", "w"))

#####################################################################################################################################



# import json


# def simpleMovingAverage(prices):

#     i = 0
#     buy = 0
#     total_profit = 0
#     first_buy = 0
#     for p in prices:
#         if i >= 5: 
#             moving_average = (prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5]) / 5
            
#             #simple moving average logic, not mean
#             if p > moving_average and buy == 0: #buy
#                 print("buying at: ", p)
#                 buy = p
#                 if first_buy == 0:
#                     first_buy = p
#             elif p < moving_average and buy != 0: #sell
#                 print("selling at: ", p)
#                 print("trade profit: ", p - buy)
#                 total_profit += p - buy
#                 buy = 0
#         i += 1
        
#     final_percentage = (total_profit / first_buy) * 100
#     print("first buy: ", first_buy)
#     print("total profit: ", total_profit)
#     print("final percentage: ", final_percentage, "%")
    
#     return total_profit, final_percentage




# ticker = ["TSLA"]
# results = {}


# fil = open("/home/ubuntu/environment/Week10/data/" + ticker[0] + ".txt")
# lines = fil.readlines()
# # print(lines)

# prices = []
# for line in lines:
#     prices.append(float(line))

# simpleMovingAverage(prices)


# profit, percentage = simpleMovingAverage(prices)
    
# results[ticker[0] + "_profit"] = round(profit,2)
# results[ticker[0] + "_returns"] = round(percentage,2)
    

# json.dump(results, open("/home/ubuntu/environment/Week10/data/results.json", "w"))


lst = []

lst = [str(item) for item in range(2,21,2)]

print(lst)


name = input("Enter your name: ")

print("welcome,", name.upper())

sentence = "dude, I just biked down that mountain and at first I was like Whoa, and then I was like Whoa"

sentence = sentence.capitalize()

sentence = sentence.split()
first = True

for i in sentence:
    if i == 'Whoa,' and first == True:
        i.lower()
        first = False
    if i == 'whoa' and first == False:
        i.upper()


sentence = " ".join(sentence)

print(sentence)







