# import libraries
import json
import numpy

# create mean reversion function
def mean_reversion(prices):
    
    # create var if stock is bought and start loop
    x = 0
    mr_total_profit = 0
    sold = 0
    bought = 0
    for p in range(len(prices)):
        
        # get current price and average
        current_price = prices[p]
        average = (prices[p - 5] + prices[p - 4] + prices[p - 3] + prices[p - 2] + prices[p - 1])/5
        
        # if it's over 5 days decide to buy or sell
        if p >= 5:
            
            # if stock is not bought and meets the requirements, buy stock and change var so stock is bought, print price bought at
            if bought == 0 and current_price < (average * 0.95):
                x += 1
                bought = current_price
                print("Buy at",bought)
                # if sold != 0 and bought != 0:
                #     trading_profit = sold - bought
                #     print("Trading Profit:", trading_profit)
                #     mr_total_profit += trading_profit  
                sold = 0
                # keep track of first buy
                if current_price == prices[-1]:
                    print("You should buy this stock today")
                if x == 1:
                    first_buy = current_price
            # if the stock is bought and and meets requrements sell and change var so stock is not bought, brint price sold at and profit from trade
            elif sold == 0 and current_price > (average * 1.05):
                sold = current_price
                print("Sell at",sold)
                if sold != 0 and bought != 0:
                    trading_profit = sold - bought
                    print("Trading Profit:", trading_profit)
                    mr_total_profit += trading_profit   
                bought = 0
                
                if current_price == prices[-1]:
                    print("You should sell this stock today")
    # round the profit and percentage to make pretty 
    mr_percentage_returns = round((mr_total_profit/first_buy)*100,2)
    mr_total_profit = round(mr_total_profit,2)
            
    # print total profit, first buy, and percentage returns 
    print("----------------")
    print("Total profit:",mr_total_profit)
    print("First buy:",round(first_buy,2))
    print("Percentage Returns: " + str(mr_percentage_returns) + "%")
    print("----------------")
    
    #return profit and returns for dictionary use
    return mr_total_profit, mr_percentage_returns

    
    
# create simple moving average function 
def simple_moving_average(prices):
    
    # create variable to keep track of if stock is bought, first buy, and profit
    stock = 0
    sma_total_profit = 0
    first_buy = 0
    x = 0
    bought = 0
    sold = 0
    # loop through stock prices and keep track of current price
    for p in range(len(prices)):
        current_price = prices[p]
        # if it's been longer that 5 days get a moving average
        if p >= 5: 
            moving_average = (prices[p-1] + prices[p-2] + prices[p-3] + prices[p-4] + prices[p-5]) / 5
            
            # if the stock is not owned and meets criteria, buy
            if current_price > moving_average and stock == 0:
                x += 1
                stock += 1
                bought = current_price
                
                print("Buy at:", bought)
                
                # short selling
                # if sold != 0 and bought != 0:
                #     trading_profit = sold - bought
                #     sma_total_profit += trading_profit
                if current_price == prices[-1]:
                    print("You should buy this stock today")
                    
                if x == 1:
                    first_buy = current_price
            
            # if stock is owned and meets criteria sell   
            elif current_price < moving_average and stock == 1:
                stock -= 1
                sold = current_price
                
                # Normal sell
                if sold != 0 and bought != 0:
                    trading_profit = sold - bought
                    sma_total_profit += trading_profit
                
                print("Sell at:", sold)
                print("Trading Profit:", trading_profit)
                
                if current_price == prices[-1]:
                    print("You should sell this stock today")
                
                sma_total_profit += trading_profit
    
    # format profit and returns and prints results and return profit and returns for dictionary use 
    sma_total_profit = round(sma_total_profit, 2)
    sma_percentage_returns = round((sma_total_profit/first_buy)*100,2)
    
    print("----------------")
    print("Total Profit:", sma_total_profit)
    print("First But:", round(first_buy,2))
    print("Percentage Returns: " + str(sma_percentage_returns) + "%")
    print("----------------")
    
    return sma_total_profit, sma_percentage_returns
                
 
def trend_algo(prices):
     
     # create variable to keep track of if stock is bought, first buy, and profit
    stock = 0
    t_total_profit = 0
    first_buy = 0
    x = 0
    bought = 0
    sold = 0
    
    
    
    # loop through stock prices and keep track of current price
    for p in range(len(prices)):
        current_price = prices[p]
        long_average = 0
        for l in range(1,36):
            long_average += prices[p-l]
        long_average = round(long_average/35,2)    
            
        # if it's been longer that 5 days get a moving average
        if p >= 5: 
            moving_average = 0
            for i in range(1,6):
                moving_average += prices[p-i]
            moving_average = round(moving_average/5,2)
            # if the stock is not owned and meets criteria, buy
            if moving_average < long_average and stock == 0:
                x += 1
                stock += 1
                bought = current_price
                
                print("Buy at:", bought)
                
                if current_price == prices[-1]:
                    print("You should buy this stock today")
                
                if x == 1:
                    first_buy = current_price
                
            # if stock is owned and meets criteria sell   
            elif moving_average > long_average and stock == 1:
                stock -= 1
                sold = current_price
                
                # Normal sell
                if sold != 0 and bought != 0:
                    trading_profit = sold - bought
                    t_total_profit += trading_profit
                
                print("Sell at:", sold)
                print("Trading Profit:", trading_profit)
                if current_price == prices[-1]:
                    print("You should sell this stock today")
                
                t_total_profit += trading_profit
    
    # format profit and returns and prints results and return profit and returns for dictionary use 
    t_total_profit = round(t_total_profit, 2)
    t_percentage_returns = round((t_total_profit/first_buy)*100,2)
    
    print("----------------")
    print("Total Profit:", t_total_profit)
    print("First But:", round(first_buy,2))
    print("Percentage Returns: " + str(t_percentage_returns) + "%")
    print("----------------")
    
    return t_total_profit, t_percentage_returns
     
     
     
     
     
     
     
            
# create list of stock ticker names and create dictionary to store results   
tickers = ["AAPL", "ADBE", "GOOG", "DOMO", "MSFT", "NVDA", "ORCL", "QCOM", "T", "TSLA"]
results = {}

# loop through stock tickers, opening them
for t in tickers:
    stonks = open("/home/ubuntu/environment/hw5/stocks/" + t + ".txt").readlines()
    # print(lines)
    
    prices = []
    # loop through each stock and add the prices to a list called prices as numbers
    for stonk in stonks:
        prices.append(float(stonk))
    # print(prices)    
    
    # print what stock and trading strategy as well as run the functions to get the returns and profits
    print("\n" + t + " Simple Moving Avg:")    
    sma_total_profit, sma_percentage_returns = simple_moving_average(prices)
    print("\n" + t + " Mean Reversion:")
    mr_total_profit, mr_percentage_returns = mean_reversion(prices)
    print("\n" + t + " Trend Algorithm:")
    t_total_profit, t_percentage_returns = trend_algo(prices)
    
    # save the profits and returns to a dictionary
    results[t + "_sma_profit"] = sma_total_profit
    results[t + "_sma_returns"] = sma_percentage_returns
    results[t + "_mr_profit"] = mr_total_profit
    results[t + "_mr_returns"] = mr_percentage_returns
    results[t + "_t_profit"] = t_total_profit
    results[t + "_t_returns"] = t_percentage_returns

# insert the results dictionary to a json file
json.dump(results, open("/home/ubuntu/environment/hw5/results.json", "w"), indent=4)
