# Import Modules
import requests
import json
import numpy
from datetime import datetime, timedelta


# Function to get data between two dates
def get_data(start_date, end_date):
    
    # Create two lists for the data
    cases = []
    dates = []
    
    # Create empty variable for the date and then turn the start date into a date
    dts = ""
    dt = datetime.strptime(start_date, '%Y-%m-%d')
    
    # while the dts(date) isn't the end date then add a day to the date and return it as a string in the right format
    while dts != end_date:
        dt += timedelta(days=1) 
        dts = dt.strftime("%Y-%m-%d")
        
        # add the cases to the cases list using the keys and date and add the date to the dates list
        cases.append(dct1[key1][key2][dts])
        dates.append(dts)

    # return both lists of data 
    return cases, dates


# Function to find the most recent date where there wasn't any new cases
def last_change(cases,dates):

    # Loop through the cases and if the difference between the current day and day before equal 0 then make that the last day there was a change
    for case in range(len(cases)):
        if cases[case] - cases[case - 1] == 0:
            last_day = cases[case]
 
    # Using the last day index and comparing it to the location in the dates we get the date and return it
    posititon = cases.index(last_day)
    last_date = dates[posititon+1]
    
    return last_date



# function for getting the average for the entire set of data
def case_average(cases):
    
    avg_list = []
    
    # loop through all the cases, taking the the next day and subracting from the current day to get the amount of cases and add them to a list
    for case in range(len(cases)-1):
        day = cases[case+1] - cases[case]
        avg_list.append(day)

    # get the average of the list using numpy functions and round it and return it
    avg = numpy.array(avg_list).mean()
    avg = round(avg,2)
    
    return avg



# function for seeing which date has the most new cases
def most_cases(cases,dates):
    
    # create lowest day
    number = 0
    
    # For each case compare it to the next day and if the total cases for that is greater than the current high then make it the high
    for case in range(len(cases)-1):
        if cases[case+1] - cases[case] > number:
            new_day = cases[case]
            number = cases[case+1] - cases[case]

    
    # Get the date on which it happened and return the date and amount of cases
    posititon = cases.index(new_day)
    highest_date = dates[posititon]
    
    return highest_date, number
    
    
    
# function to get the month with hightest number of cases and lowest
def each_month():
    
    # Get the ranges for each month starting at the end the the first month because it starts one day after
    months = [["2020-01-21","2020-01-31"],["2020-01-31","2020-02-29"],["2020-02-29","2020-03-31"],["2020-03-31","2020-04-30"],["2020-04-30","2020-05-31"],["2020-05-31","2020-06-30"],["2020-06-30","2020-07-31"],["2020-07-31","2020-08-31"],["2020-08-31","2020-09-30"],["2020-09-30","2020-10-31"],["2020-10-31","2020-11-30"],["2020-11-30","2020-12-31"]]
    months.extend([["2020-12-31","2021-01-31"],["2021-01-31","2021-02-28"],["2021-02-28","2021-03-31"],["2021-03-31","2021-04-30"],["2021-04-30","2021-05-31"],["2021-05-31","2021-06-30"],["2021-06-30","2021-07-31"],["2021-07-31","2021-08-31"],["2021-08-31","2021-09-30"],["2021-09-30","2021-10-31"],["2021-10-31","2021-11-30"],["2021-11-30","2021-12-31"]])
    
    # create counter and empty dictionary and list with each month
    i = 0
    month_results = {}
    monthly_name = ["Jan 2020", "Feb 2020", "March 2020", "April 2020", "May 2020", "June 2020", "July 2020", "Aug 2020", "Sep 2020", "Oct 2020", "Nov 2020", "Dec 2020", "Jan 2021", "Feb 2021", "March 2021", "April 2021", "May 2021", "June 2021", "July 2021", "Aug 2021", "Sep 2021", "Oct 2021", "Nov 2021", "Dec 2021"]
    
    # loop through each month adding to the counter
    for month in months:
        i += 1
        num_cases = 0
        
        # get the start and end date of each month and get the data for that month
        start_date = month[0]
        end_date = month[1]
        cases, dates = get_data(start_date, end_date)
        
        # loop through the cases and get the amount of cases per day and add it so a variable
        for j in range(len(cases) - 1):
            num_cases += cases[j+1] - cases[j]
        
        # add the number of cases to each month in the dictionary
        month_results[monthly_name[i-1]] = num_cases

    # get the high and low month as well as the numbers for both and return them
    highest_month = max(month_results, key=month_results.get)
    lowest_month = min(month_results, key=month_results.get)
    high_num = month_results.get(highest_month)
    low_num = month_results.get(lowest_month)
    
    return highest_month, lowest_month, high_num, low_num
    
        
        
# get the average of each month
def each_month_avg():
    
    # Get the ranges for each month starting at the end the the first month because it starts one day after
    months = [["2020-01-21","2020-01-31"],["2020-01-31","2020-02-29"],["2020-02-29","2020-03-31"],["2020-03-31","2020-04-30"],["2020-04-30","2020-05-31"],["2020-05-31","2020-06-30"],["2020-06-30","2020-07-31"],["2020-07-31","2020-08-31"],["2020-08-31","2020-09-30"],["2020-09-30","2020-10-31"],["2020-10-31","2020-11-30"],["2020-11-30","2020-12-31"]]
    months.extend([["2020-12-31","2021-01-31"],["2021-01-31","2021-02-28"],["2021-02-28","2021-03-31"],["2021-03-31","2021-04-30"],["2021-04-30","2021-05-31"],["2021-05-31","2021-06-30"],["2021-06-30","2021-07-31"],["2021-07-31","2021-08-31"],["2021-08-31","2021-09-30"],["2021-09-30","2021-10-31"],["2021-10-31","2021-11-30"],["2021-11-30","2021-12-31"]])
    
    # create counter and empty dictionary and list with each month
    i = 0
    month_results = {}
    monthly_name = ["Jan 2020", "Feb 2020", "March 2020", "April 2020", "May 2020", "June 2020", "July 2020", "Aug 2020", "Sep 2020", "Oct 2020", "Nov 2020", "Dec 2020", "Jan 2021", "Feb 2021", "March 2021", "April 2021", "May 2021", "June 2021", "July 2021", "Aug 2021", "Sep 2021", "Oct 2021", "Nov 2021", "Dec 2021"]
    
    # Loop through each month and get the data for both
    for month in months:
        start_date = month[0]
        end_date = month[1]
        i += 1
        cases, dates = get_data(start_date, end_date)
        
        # using the previous function of getting the average and add each months average to the dictionary
        month_results[monthly_name[i-1]] = case_average(cases)
    
    # Get the high and low month and the average for each and return them
    highest_month = max(month_results, key=month_results.get)
    lowest_month = min(month_results, key=month_results.get)
    high_num = month_results.get(highest_month)
    low_num = month_results.get(lowest_month)
    
    return highest_month, lowest_month, high_num, low_num



# Create list for the countries
countries = ["US", "Russia", "Italy"]


# Loop through countries
for country in countries:
    
    # Get the url and keys
    url = 'https://covid-api.mmediagroup.fr/v1/history?country='+country+'&status=confirmed'
    key1 = "All"
    key2 = "dates"

    # Start getting data
    req = requests.get(url)

# get the data and put it in a dictionary
    dct1 = json.loads(req.text)
    
    # start and end date and create empty dictionary
    end_date = "2021-12-31"
    start_date = "2020-01-21"
    results = {}

    # print results for what country
    print()
    print("Covid confirmed cases stats")
    results["Country Name"] = country
    print("Country Name:", country)
    
    # Get the data from the functions
    get_data(start_date,end_date)
    cases, dates = get_data(start_date, end_date)
    highest_month, lowest_month, high_num, low_num = each_month()
    highest_date, number = most_cases(cases,dates)
    
    # Print results for each and then add them to a dictionary
    print("Average Number of Cases for whole set:", case_average(cases))
    results["Average Number of Cases for whole set"] = case_average(cases)
    
    print("Date with highest new number of confirmed cases:", highest_date, "# of cases:", number)
    results["Date with highest new number of confirmed cases"] = highest_date
    
    print("Most recent date with no new cases:", last_change(cases,dates))
    results["Most recent date with no new cases"] = last_change(cases,dates)
    
    print("Month with highest new number of confirmed cases:", highest_month, "# of cases:", high_num)
    results["Month with highest new number of confirmed cases"] = highest_month
    
    print("Month with lowest number of confirmed cases:", lowest_month, "# of cases:", low_num)
    results["Month with lowest number of confirmed cases"] = lowest_month
    
    highest_month, lowest_month, high_num, low_num = each_month_avg()
    print("Month with highest average cases:", highest_month, "avg cases:", high_num)
    results["Month with highest average cases"] = highest_month
    
    print("Month with lowest average cases:", lowest_month, "avg cases:", low_num)
    results["Month with lowest average cases"] = lowest_month
    
    # put the dictionary into a json
    json.dump(results, open("/home/ubuntu/environment/HW3/"+country+".json", "w"), indent=4)





