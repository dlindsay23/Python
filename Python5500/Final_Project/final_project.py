# Import Modules
import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import REST, TimeFrame, TimeFrameUnit
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import pandas as pd
import requests
import json
import time


today = datetime.today()

# Month abbreviation, day and year	
date1 = today.strftime("%Y-%m-%d")
date2 = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')


# Get info for connecting to api
BASE_URL = "https://paper-api.alpaca.markets"
ALPACA_API_KEY = "PKFQD2N1W208HIHWESX7"
ALPACA_SECRET_KEY = "MUzln9YUlwVpMFN2Ib9oiEjFPeKfM3tW0WCo7m4V"

# Used to connect to the api
api = tradeapi.REST(key_id=ALPACA_API_KEY, secret_key=ALPACA_SECRET_KEY, 
                    base_url=BASE_URL, api_version='v2')


# This is for getting the historical data. I limited the data to 2017 to now, didn't see the sense in going back any further for relevancy.
def historical_date(stocks):

# loop through each stock ticker
    for stock in stocks:
        
        # Used to get the data for each stock and throw it into the data frame. Printing the stock and the beginning and end of the data frame to make sure
        # it includes all the data
        hstry_data = api.get_bars(stock, TimeFrame.Day, "2017-01-01" ,"2022-01-01", adjustment='raw').df
        time.sleep(2)
        print(stock)
        df = pd.DataFrame(hstry_data)
        print(df.head())
        
        # Taking the timestamp out of the index and then changing it to just the date and excluding the time
        df.reset_index(inplace=True)
        print(df.head())
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['Date'] = df['timestamp'].dt.date
        
        print("\n")
        
        # create a new data frame off of the old one where we only keep the closing price and date for the stock and print so we know what it looks like
        new = df[['Date', 'close']]
        print(new.head())
        
        # Put the date and price into a csv
        new.to_csv('/home/ubuntu/environment/Final_Project/Data/'+stock+'.csv', index=False)


# Used to append the latest data to the csv. Where aplaca doesn't allow me to get todays data all my trades are based off the close of yesterdays data
def append_data(stocks):
    print("Updating Data...")
    for stock in stocks:
        # print(stock)
        
         # get last day we updated each csv/stock
        last_day = open('/home/ubuntu/environment/Final_Project/Data/'+stock+'.csv').readlines()[-1].split(",")[0]
        last_day = datetime.strptime(last_day, '%Y-%m-%d')
        last_day = datetime.strftime(last_day + timedelta(1), '%Y-%m-%d')

        
        appnd_data = api.get_bars(stock, TimeFrame.Day, last_day ,date2, adjustment='raw').df
        time.sleep(.5)
        
        if appnd_data.empty == False:
            df = pd.DataFrame(appnd_data)
    
            
            # Taking the timestamp out of the index and then changing it to just the date and excluding the time
            df.reset_index(inplace=True)
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df['Date'] = df['timestamp'].dt.date
            
            # print("\n")
            
            # create a new data frame off of the old one where we only keep the closing price and date for the stock and print so we know what it looks like
            new = df[['Date', 'close']]
            # print(new.head())
            
            new.to_csv('/home/ubuntu/environment/Final_Project/Data/'+stock+'.csv', mode='a', index=False, header=False)



# This algorithm is kind of a take on looking at the trends of a stock. Basically if the 20 day moving average is less than the 50 day moving average buy and if its more then sell.
# I messed around with what averages to use and this is one that got me the best returns from my testing.
def trend_algo(prices):
     
    # create variable to keep track of if stock is bought, first buy, and profit
    stock = 0
    t_total_profit = 0
    first_buy = 0
    x = 0
    bought = 0
    sold = 0
    t_buy_today = 0
    t_sell_today = 0
    
    # loop through stock prices and keep track of current price
    for p in range(len(prices)):
        current_price = prices[p]
        long_average = 0
        
        # Get the 50 day moving average
        for l in range(1,51):
            long_average += prices[p-l]
        long_average = round(long_average/50,2)    
            
        # if it's been longer that 20 days get a moving average
        if p >= 5: 
            moving_average = 0
            for i in range(1,21):
                moving_average += prices[p-i]
            moving_average = round(moving_average/20,2)
            
            # if the stock is not owned and meets criteria, buy
            if moving_average < long_average and stock == 0:
                x += 1
                stock += 1
                bought = current_price
                
                # Check to see if you should buy today
                if current_price == prices[-1]:
                    t_buy_today = 1
                    
                # Keep track of first buy 
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
                
                # Check to see if you should sell today
                if current_price == prices[-1]:
                    t_sell_today = 1
                
                t_total_profit += trading_profit
    
    # format profit and returns and prints results and return profit and returns for dictionary use  as well as if you should buy or sell today
    t_total_profit = round(t_total_profit, 2)
    t_percentage_returns = round((t_total_profit/first_buy)*100,2)
    
    
    print("----------------")
    print("Total Profit:", t_total_profit)
    print("First But:", round(first_buy,2))
    print("Percentage Returns: " + str(t_percentage_returns) + "%")
    print("----------------")
    
    return t_total_profit, t_percentage_returns, t_buy_today, t_sell_today
    
    
    
    
    
    
# create simple moving average function 
def simple_moving_average(prices):
    
    # create variable to keep track of if stock is bought, first buy, and profit
    stock = 0
    sma_total_profit = 0
    first_buy = 0
    x = 0
    sma_buy_today = 0
    sma_sell_today = 0
    
    # loop through stock prices and keep track of current price
    for price in range(len(prices)):
        current_price = prices[price]
        
        # if it's been longer that 5 days get a moving average
        if price >= 5: 
            moving_average = (prices[price - 1] + prices[price - 2] + prices[price - 3] + prices[price - 4] + prices[price - 5]) / 5
            
            # if the stock is not owned and meets criteria, buy
            if current_price > moving_average and stock == 0:
                x += 1
                stock += 1
                bought = current_price
                

                # Check to see if you should buy today
                if current_price == prices[-1]:
                    sma_buy_today = 1
                
                # keep track of first buy
                if x == 1:
                    first_buy = current_price
            
            # if stock is owned and meets criteria sell   
            elif current_price < moving_average and stock == 1:
                stock -= 1
                sold = current_price
                trading_profit = sold - bought
                
                # Check to see if you should sell today
                if current_price == prices[-1]:
                    sma_sell_today = 1
                
                sma_total_profit += trading_profit
    
    # format profit and returns and prints results and return profit and returns for dictionary use 
    sma_total_profit = round(sma_total_profit, 2)
    sma_percentage_returns = round((sma_total_profit/first_buy)*100,2)
    
    print("----------------")
    print("Total Profit:", sma_total_profit)
    print("First But:", round(first_buy,2))
    print("Percentage Returns: " + str(sma_percentage_returns) + "%")
    print("----------------")
    
    return sma_total_profit, sma_percentage_returns, sma_buy_today, sma_sell_today
    
    
    
    
# create mean reversion strategy
def mean_reversion(prices):
    
    # create var if stock is bought and start loop
    stock = 0
    x = 0
    mr_total_profit = 0
    mr_buy_today = 0
    mr_sell_today = 0
    # I forgot to add the sold variable back so now it works
    sold = 0
    for price in range(len(prices)):
        
        # get current price and average
        current_price = prices[price]
        average = (prices[price - 5] + prices[price - 4] + prices[price - 3] + prices[price - 2] + prices[price - 1])/5
        
        # if it's over 5 days decide to buy or sell
        if price >= 5:
            
            # if stock is not bought and meets the requirements, buy stock and change var so stock is bought, print price bought at
            if stock == 0 and current_price < (average * 0.95):
                stock += 1
                x += 1
                bought = current_price
                
                # short selling
                if sold != 0 and bought != 0:
                    trading_profit = sold - bought
                    mr_total_profit += trading_profit
                
                # check to see if you should buy today
                if current_price == prices[-1]:
                    mr_buy_today = 1
                    
                # keep track of first buy
                if x == 1:
                    first_buy = current_price
                    
            # if the stock is bought and and meets requrements sell and change var so stock is not bought, update trading profit
            elif stock == 1 and current_price > (average * 1.05):
                stock -= 1
                sold = current_price
                trading_profit = sold - bought
                mr_total_profit += trading_profit 
                
                # Check to see if you should sell today
                if current_price == prices[-1]:
                    mr_sell_today = 1
                    
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
    return mr_total_profit, mr_percentage_returns, mr_buy_today, mr_sell_today
    
    
    
# Create list of tickers and empty lists and dictionary for later use 
tickers = ['MCHP', 'NVDA', 'SPXL', 'AAPL', 'ORCL', 'QCOM', 'KMI', 'T', 'MSFT', 'AMZN']
results = {}
sma_buy_lst = []
sma_sell_lst = []
sma_hold_lst = []
mr_buy_lst = []
mr_sell_lst = []
mr_hold_lst = []
t_buy_lst = []
t_sell_lst = []
t_hold_lst = []

# I ran this the first time to be able to create the csv and add historical data
# historical_date(tickers)


# This is ran everytime to get current data
append_data(tickers)
input("Press enter to continue...")
# Loop through all the tickers and carry out trading
for t in tickers:
    
    stonks = open("/home/ubuntu/environment/Final_Project/Data/" + t + ".csv").readlines()
    prices = []
    dates = []
    
    # Get just the prices from each and create a list of them
    for price in range(len(stonks)):
        if price > 0:
            high = stonks[price].split(',')[1]
            date = stonks[price].split(',')[0]
            prices.append(float(high))
            dates.append(date)

    
    # Experimenting with graphing the stock price but it slows down the program more than i'd like
    # plt.plot(dates, prices)
    # plt.title('Stock graph')
    # plt.savefig("/home/ubuntu/environment/Final_Project/Graphs/"+t+".png")
    # plt.clf()
    
     # print what stock and trading strategy as well as run the functions to get the returns and profits and whether to buy or sell
    print("\n" + t + " Simple Moving Avg:")    
    sma_total_profit, sma_percentage_returns, sma_buy_today, sma_sell_today = simple_moving_average(prices)
    print("\n" + t + " Mean Reversion:")
    mr_total_profit, mr_percentage_returns, mr_buy_today, mr_sell_today = mean_reversion(prices)
    print("\n" + t + " Trend Algorithm:")
    t_total_profit, t_percentage_returns, t_buy_today, t_sell_today = trend_algo(prices)
    
    # for each strategy, look and see if we should buy sell or hold the stock today and put the results into a list
    if sma_buy_today == 1:
        sma_buy_lst.append(t)
    elif sma_sell_today == 1:
        sma_sell_lst.append(t)
    else:
        sma_hold_lst.append(t)
        
    if mr_buy_today == 1:
        mr_buy_lst.append(t)
    elif mr_sell_today == 1:
        mr_sell_lst.append(t)
    else:
        mr_hold_lst.append(t)
    
    
    # I chose this strategy to be my actual ordering because it had on average the greatest returns for each stock. Where most of the time this is
    # going to be a hold I bought all the stocks first and now it will sell or buy according to this trend.
    if t_buy_today == 1:
        t_buy_lst.append(t)
        
        # Get position on stock. If already owned then don't buy another one to prevent buying the same stock.
        # Still showing the stock on the list of stocks to buy even if it's already bought.
        position = api.get_position(t)
        if position.qty == 0:
            api.submit_order(
                symbol=t,
                qty=1,
                side='buy',
                type='market',
                time_in_force='day',
            )
    elif t_sell_today == 1:
        t_sell_lst.append(t)
        
        # If stock is already bought then we can sell it. We don't want to be selling stocks we don't have. We'd be short selling.
        # Still showing the stock on the list of stocks to sell even if it's already sold.
        position = api.get_position(t)
        if position.qty == 1:
            api.submit_order(
                symbol=t,
                qty=1,
                side='sell',
                type='market',
                time_in_force='day',
            )
    else:
        t_hold_lst.append(t)
    

    # save the profits and returns to a dictionary
    results[t + "_sma_profit"] = sma_total_profit
    results[t + "_sma_returns"] = sma_percentage_returns
    results[t + "_mr_profit"] = mr_total_profit
    results[t + "_mr_returns"] = mr_percentage_returns
    results[t + "_t_profit"] = t_total_profit
    results[t + "_t_returns"] = t_percentage_returns
    
    
# insert the results dictionary to a json file
json.dump(results, open("/home/ubuntu/environment/Final_Project/results.json", "w"), indent=4)

# Print what to do with the stock today for each strategy
print("\nWhat you should do with the stocks today:")
print("SMA Buy List",sma_buy_lst)
print("SMA Sell List",sma_sell_lst)
print("SMA Hold List",sma_hold_lst)
print("-------------------------")
print("MR Buy List",mr_buy_lst)
print("MR Sell List",mr_sell_lst)
print("MR Hold List",mr_hold_lst)
print("-------------------------")
print("Trend Buy List",t_buy_lst)
print("Trend Sell List",t_sell_lst)
print("Trend Hold List",t_hold_lst)

# Look in the dictionary to see what the biggest value is and return it.
print("\nThe Strategy and stock thats made the biggest returns: ", end="")
highest_return = max(results, key=results.get)
print(highest_return)

