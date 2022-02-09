

lst = open("hw4/aapl.txt").readlines()


for num in range(len(lst)):
    lst[num] = float(lst[num])
    lst[num] = round(lst[num], 2)

# create var if stock is bought and start loop
stock = 0
x = 0
total_profit = 0
for i in range(len(lst)):
    
    # get current price and average
    current_price = lst[i]
    average = (lst[i - 5] + lst[i - 4] + lst[i - 3] + lst[i - 2] + lst[i - 1])/5
    
    # if it's over 5 days decide to buy or sell
    if i >= 5:
        
        # if stock is not bought and meets the requirements, buy stock and change var so stock is bought, print price bought at
        if stock == 0 and current_price < (average * 0.95):
            stock += 1
            x += 1
            bought = current_price
            print("Buy at",bought)
            # keep track of first buy
            if x == 1:
                first_buy = current_price
        # if the stock is bought and and meets requrements sell and change var so stock is not bought, brint price sold at and profit from trade
        elif stock == 1 and current_price > (average * 1.05):
            stock -= 1
            sold = current_price
            print("Sell at",sold)
            trading_profit = sold - bought
            print("Trading Profit:", round(trading_profit,2))
            total_profit += trading_profit    
        
# print total profit, first buy, and percentage returns 
print("----------")
print("Total profit:",round(total_profit,2))
print("First buy:",first_buy)
print("Percentage Returns: " + str(round((total_profit/first_buy)*100,2)) + "%")








